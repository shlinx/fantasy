import os
import requests
from django.core.management.base import BaseCommand, CommandError
from ...models import TNZRawListing, TNZTag


class Command(BaseCommand):
    help = 'Fetch listings.'

    api_key = os.environ.get('API_KEY')
    base_url = 'http://www.newzealand.com/api/rest/v1/deliver/listings?level=full&maxrows=30'

    def add_arguments(self, parser):
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

    def fetch(self, url: str, debug: bool = False):

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
                'unique_id': listing['unique_id'],
                'market': listing['market'],
                'data': str(listing)
            }
            existings = TNZRawListing.objects.filter(unique_id=listing['unique_id'])
            if not existings.exists():
                TNZRawListing.objects.create(**listing_data)
                imported += 1
                if debug:
                    self.stdout.write('Imported {name}'.format(name=listing['nameoflisting']))
            else:
                existings.update(**listing_data)
                updated += 1
                if debug:
                    self.stdout.write('Updated {name}'.format(name=listing['nameoflisting']))
        else:
            self.stdout.write('Successfully imported {imported} listing(s), updated {updated} listing(s)'
                              .format(imported=imported, updated=updated))
            if data['link']['next']:
                self.fetch(data['link']['next'], debug)
