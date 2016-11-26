import os
import requests
from django.core.management.base import BaseCommand, CommandError
from ...models import TNZRegion


class Command(BaseCommand):
    help = 'Fetch regions'

    can_import_settings = True
    api_key = os.environ.get('API_KEY')
    base_url = 'http://www.newzealand.com/api/rest/v1/deliver/regions?level=simple'

    def add_arguments(self, parser):
        parser.add_argument(
            '--market',
            nargs=1,
            dest='market',
            help='Specify market name. Default: en'
        )
        parser.add_argument(
            '--debug',
            action='store_true',
            dest='debug',
            default=False,
            help='Show debug output information',
        )

    def handle(self, *args, **options):
        """
        Implement the handle method
        :param args:
        :param options:
        :return:
        """
        if options['market']:
            init_url = self.base_url + '&display_market=' + options['market'][0]
        else:
            init_url = self.base_url

        try:
            self.fetch(url=init_url, debug=options['debug'])
        except CommandError:
            raise

    def fetch(self, url: str = base_url, debug: bool = False) -> None:
        """
        Recursively fetch all regions
        :param url:
        :param debug:
        :return:
        """
        self.stdout.write('Fetching from {0}'.format(url))

        imported = 0
        updated = 0
        res = requests.get(url, headers={'Authorization': 'Bearer ' + self.api_key})
        if res.status_code != 200:
            raise requests.HTTPError('Fetching data fail', res.status_code)

        data = res.json()

        for region in data['items']:
            existings = TNZRegion.objects.filter(name_key=region['name_key'])
            if not existings.exists():
                TNZRegion.objects.create(**region)
                imported += 1
                if debug:
                    self.stdout.write('{0} written'.format(region['name_key']))
            else:
                existings.update(**region)
                updated += 1
                if debug:
                    self.stdout.write('{0} exists, updated'.format(region['name_key']))
        else:
            self.stdout.write('Successfully imported {imported} region(s), updated {updated} region(s).'
                              .format(imported=imported, updated=updated))
            if data['link']['next'] != '':
                self.fetch(data['link']['next'])
