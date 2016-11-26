import os
import requests
from django.core.management.base import BaseCommand, CommandError
from ...models import RawListing


class Command(BaseCommand):
    help = 'Fetch listings.'

    api_key = os.environ.get('API_KEY')
    base_url = 'http://www.newzealand.com/api/rest/v1/deliver/listings?level=full&maxrows=30'

    def add_arguments(self, parser):
        parser.add_argument(
            'tag',
            help='Specify a tag name'
        )
        parser.add_argument(
            '--debug',
            action='store_true',
            default=False,
            dest='debug',
            help='Show debug output information'
        )

    def handle(self, *args, **options):
        url = self.base_url + '&tag=' + options['tag']
        self.fetch(url=url, debug=options['debug'])

    def fetch(self, url: str, debug: bool = False):

        imported = 0
        skipped = 0

        self.stdout.write('Fetching from {0}'.format(url))
        res = requests.get(url, headers={'Authorization': 'Bearer ' + self.api_key})

        if res.status_code != 200:
            raise requests.HTTPError('Fetching data fail', res.status_code)

        data = res.json()

        for listing in data['items']:
            if not RawListing.objects.filter(unique_id=listing['unique_id']).exists():
                listing_data = {
                    'name': listing['nameoflisting'],
                    'unique_id': listing['unique_id'],
                    'data': str(listing)
                }
                RawListing.objects.create(**listing_data)
                imported += 1
                if debug:
                    self.stdout.write('Imported {name}'.format(name=listing['nameoflisting']))
            else:
                skipped += 1
                if debug:
                    self.stdout.write('Skipped {name}'.format(name=listing['nameoflisting']))
        else:
            self.stdout.write('Successfully imported {imported} listing(s), skipped {skipped} listing(s)'
                              .format(imported=imported, skipped=skipped))
            if data['link']['next']:
                self.fetch(data['link']['next'], debug)
