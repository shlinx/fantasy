import os
import requests
from django.core.management.base import BaseCommand, CommandError
from ...models import RawTag


class Command(BaseCommand):

    can_import_settings = True

    help = 'Fetch tags'
    api_key = os.environ.get('API_KEY')
    default_tag_url = 'http://www.newzealand.com/api/rest/v1/deliver/tags/listingcount'

    def add_arguments(self, parser):
        parser.add_argument('debug', type=bool, nargs='?')

    def handle(self, *args, **options):
        self.fetch(debug=options['debug'])

    def fetch(self, url: str = default_tag_url, debug: bool = False) -> None:
        """
        Recursively fetch all tags
        :param url:
        :param debug:
        :return:
        """
        self.stdout.write('Fetching from {0}'.format(url))

        imported = 0
        skipped = 0
        res = requests.get(url, headers={'Authorization': 'Bearer ' + self.api_key})
        if res.status_code != 200:
            raise requests.HTTPError('Fetching data fail', res.status_code)

        data = res.json()

        for tag in data['items']:
            if not RawTag.objects.filter(name_key=tag['name_key']).exists():
                tag_data = {
                    'name_key': tag['name_key'],
                    'label': tag['label'],
                    'data': str(tag)
                }
                RawTag.objects.create(**tag_data)
                imported += 1
                if debug:
                    self.stdout.write('{0} written'.format(tag['name_key']))
            else:
                skipped += 1
                if debug:
                    self.stdout.write('{0} exists, skipped'.format(tag['name_key']))
        else:
            self.stdout.write('Successfully imported {0} tags, skipped {1} tags.'.format(imported, skipped))
            if data['link']['next'] != '':
                self.fetch(data['link']['next'])
