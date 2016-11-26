import os
import requests
from django.core.management.base import BaseCommand, CommandError
from ...models import TNZTag


class Command(BaseCommand):
    help = 'Fetch tags'

    can_import_settings = True
    api_key = os.environ.get('API_KEY')
    default_url = 'http://www.newzealand.com/api/rest/v1/deliver/tags/listingcount?display_market=cn'

    def add_arguments(self, parser):
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
        try:
            self.fetch(debug=options['debug'])
        except CommandError:
            raise

    def fetch(self, url: str = default_url, debug: bool = False) -> None:
        """
        Recursively fetch all tags
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

        for tag in data['items']:
            existings = TNZTag.objects.filter(name_key=tag['name_key'])
            if not existings.exists():
                TNZTag.objects.create(**tag)
                imported += 1
                if debug:
                    self.stdout.write('{0} written'.format(tag['name_key']))
            else:
                existings.update(**tag)
                updated += 1
                if debug:
                    self.stdout.write('{0} exists, updated'.format(tag['name_key']))
        else:
            self.stdout.write('Successfully imported {imported} tag(s), updated {updated} tag(s).'
                              .format(imported=imported, updated=updated))
            if data['link']['next'] != '':
                self.fetch(data['link']['next'])
