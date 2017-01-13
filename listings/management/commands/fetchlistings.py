"""
The management command for fetching TNZ listings.
Example: python manage.py --tags tag1 tag2 --market cn
You can use --debug to output more information
"""
import datetime
import requests

from django.core.management.base import BaseCommand
from django.conf import settings
from django.utils import timezone

from ...models import TNZListing, TNZTag


class Command(BaseCommand):
    """
    The TNZ listings fetcher
    """
    help = 'Fetch listings.'

    api_key = settings.API_KEY
    base_url = 'http://www.newzealand.com/api/rest/v1/deliver/listings?level=full&maxrows=30'

    def add_arguments(self, parser):
        """
        Add arguments for command
        :param parser:
        :return:
        """
        parser.add_argument(
            '--tags',
            dest='tags',
            nargs='+',
            help='Specify tag names'
        )
        parser.add_argument(
            '--market',
            dest='market',
            nargs=1,
            help='Specify market name. Default: en'
        )
        parser.add_argument(
            '--debug',
            action='store_true',
            default=False,
            dest='debug',
            help='Show debug output information'
        )

    def handle(self, *args, **options):
        """
        Handle the command
        :param args:
        :param options:
        :return:
        """
        if len(options['market']):
            url_wo_tag = self.base_url + '&display_market=' + options['market'][0]
        else:
            url_wo_tag = self.base_url
        if options['tags'] is None:
            tags = TNZTag.objects.order_by('-listing_count').values_list('name_key', flat=True)
        else:
            tags = options['tags']

        for tag in tags:
            url = url_wo_tag + '&tag=' + tag
            self.fetch(url=url, debug=options['debug'])

    def fetch(self, url: str, debug: bool=False):
        """
        Fetch listings from url
        :param url:
        :param debug:
        :return:
        """
        imported = 0
        updated = 0

        self.stdout.write('Fetching from {0}'.format(url))
        res = requests.get(url, headers={'Authorization': 'Bearer ' + self.api_key})

        if res.status_code != 200:
            raise requests.HTTPError('Fetching data fail', res.status_code)

        data = res.json()

        for listing in data['items']:
            listing_data = {
                'name': listing['nameoflisting'],
                'modified_date': timezone.make_aware(datetime.datetime.strptime(
                    listing['modified_date'], '%B, %d %Y %X')
                ),
                'main_image': listing['assets'].get('main'),
                'logo_image': listing['assets'].get('logo'),
                # gallery image can be null
                'gallery_images': listing['assets'].get('gallery'),
                'regionname': listing['regionname'],
                'unique_id': listing['unique_id'],
                'market': listing['market'],
                'listing_description': listing['listing_description'],
                'listing_summary': listing['listing_summary'],
                'latitude': listing['latitude'],
                'longitude': listing['longitude'],
                'business_type': listing['business_type'],
                'minimum_age': listing['minimum_age'],
                'max_capacity': listing['max_capacity'],
                'website_link': listing['website_link'],
                'booking_link': listing['booking_link'],
                'phone': listing['phone'],
                'mobile': listing['mobile'],
                'email': listing['email'],
                'operational_hours': listing['operational_hours'],
                'street': listing['street'],
                'suburb': listing['suburb'],
                'city': listing['city'],
                'postcode': listing['postcode'],
                'proximity_to_town': listing['proximity_to_town'],
                'proximity_to_airport': listing['proximity_to_airport'],
                'freephone': listing['freephone'],
                'tags': listing['tags'],
                'listing_types': listing['listing_types'],
                'booking_email': listing['booking_email'],
                'cancellation_policy': listing['cancellation_policy'],
                'parking': listing['parking'],
            }

            existings = TNZListing.objects.filter(unique_id=listing['unique_id'])
            if not existings.exists():
                TNZListing.objects.create(**listing_data)
                imported += 1
                if debug:
                    self.stdout.write('Imported {name}'.format(name=listing['nameoflisting']))
            else:
                existings.update(**listing_data)
                updated += 1
                if debug:
                    self.stdout.write('Updated {name}'.format(name=listing['nameoflisting']))
        self.stdout.write('Successfully imported {imported} listing(s),'
                          ' updated {updated} listing(s)'
                          .format(imported=imported, updated=updated))
        if data['link']['next']:
            self.fetch(data['link']['next'], debug)


def extract_image(original_data):
    """
    Extract image from the original data
    :param original_data:
    :return:
    """
    image_data = {
        'o_id': original_data['o_id'],
        'description': original_data['description'],

    }

    return image_data
