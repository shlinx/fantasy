from __future__ import absolute_import, unicode_literals

from django.db.models import Count
from django.http import HttpResponse
from wagtail.wagtailcore.models import Page
from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin, route

from listings.models import TNZListing


class HomePage(RoutablePageMixin, Page):
    listings = TNZListing.objects.all()[:12]

    @route(r'^search/$', name='search')
    def search(self, request):
        print(request.POST)
        return HttpResponse(request.POST)

    @route(r'^filter/$', name='filter')
    def filter(self, request):
        print(request.POST)
        return HttpResponse(request.POST)

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
    def business_types():
        """
        Get business types data.
        :return:
        """
        business_types_data = []
        business_types_map = {
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
            if value in business_types_map:
                business_types_data.append({
                    'value': value,
                    'label': business_types_map[value]
                })
                continue
            business_types_data.append({
                'value': value,
                'label': value
            })
        return business_types_data

