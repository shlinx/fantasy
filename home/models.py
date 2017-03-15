from __future__ import absolute_import, unicode_literals
from urllib.parse import urlencode
from django.db.models import Count
from django.urls import reverse
from django.shortcuts import redirect
from wagtail.wagtailcore.models import Page
from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin, route

from listings.models import TNZListing


class HomePage(RoutablePageMixin, Page):
    listings = TNZListing.objects.all()[:12]

    @route(r'^search/$', name='search')
    def search(self, request):
        """
        Request handler for searching keyword.
        :param request:
        :return:
        """
        query = ''
        keyword = request.POST.get('keyword')
        if keyword:
            query = '?' + urlencode({
                'keyword': keyword
            })

        return redirect(reverse('search') + query)

    @route(r'^filter/$', name='filter')
    def filter(self, request):
        """
        Request handler for filtering by region and type.
        :param request:
        :return:
        """
        query = ''
        query_data = {}
        has_query = False
        for key in ('regions', 'types'):
            value = request.POST.get(key)
            if value:
                query_data[key] = value
                has_query = True

        if has_query:
            query = '?' + urlencode(query_data)

        return redirect(reverse('search') + query)

    @staticmethod
    def regions():
        """
        Get regions data.
        :return:
        """
        regions_data = []
        region_map = {
            '': '其他',
            'Clutha': '克卢撒',
            'Waitaki': '怀塔基',
            'Stewart Island - Rakiura': '斯图尔特岛 - 拉奇欧拉'
        }
        for region in TNZListing.objects.values('regionname').annotate(count=Count('id')).order_by('-count'):
            regionname = region['regionname']
            if regionname in region_map:
                regions_data.append({
                    'regionname': regionname,
                    'label': region_map[regionname]
                })
                continue
            regions_data.append({'regionname': regionname, 'label': regionname})
        return regions_data

    @staticmethod
    def types():
        """
        Get business types data.
        :return:
        """
        types_data = []
        types_map = {
            'Accommodation': '住宿',
            'Activities and Tours': '观光活动',
            'Transport': '交通',
            'Visitor Information Centre': '信息中心',
            'Online Information Service': '在线信息服务',
            'Travel Agent or Airline': '旅行中介或空运',
            'Airline': '空运',
            'Online Booking Service': '在线订票服务',
            'Travel Agent': '旅行中介',
        }
        for business_type in TNZListing.objects.values('business_type').annotate(count=Count('id')).order_by('-count'):
            value = business_type['business_type']
            if value in types_map:
                types_data.append({
                    'value': value,
                    'label': types_map[value]
                })
                continue
            types_data.append({
                'value': value,
                'label': value
            })
        return types_data

