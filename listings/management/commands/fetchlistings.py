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

from ...models import TNZListing, TNZTag, TNZImage, TNZImageInstance


class Command(BaseCommand):
    """
    The TNZ listings fetcher
    """
    help = 'Fetch listings.'

    api_key = settings.API_KEY
    base_url = 'http://www.newzealand.com/api/rest/v1/deliver/listings?level=full&maxrows=30'

    UNCHANGED = 0
    IMPORTED = 1
    UPDATED = 2

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
        unchanged = 0

        self.stdout.write('Fetching from {0}'.format(url))
        res = requests.get(url, headers={'Authorization': 'Bearer ' + self.api_key})

        if res.status_code != 200:
            raise requests.HTTPError('Fetching data fail', res.status_code)

        data = res.json()

        for listing_data in data['items']:
            listing, flag = self.save_listing(listing_data)

            if flag == self.IMPORTED:
                imported += 1
                if debug:
                    self.stdout.write('Imported "{name}".'.format(name=listing.name))
            elif flag == self.UPDATED:
                updated += 1
                if debug:
                    self.stdout.write('Updated "{name}".'.format(name=listing.name))
            elif flag == self.UNCHANGED:
                unchanged += 1
                if debug:
                    self.stdout.write('"{name}" not changed.'.format(name=listing.name))
        self.stdout.write('Successfully imported {imported} listing(s),'
                          ' updated {updated} listing(s),'
                          ' {unchanged} listing(s) unchanged.'
                          .format(imported=imported, updated=updated, unchanged=unchanged))
        if data['link']['next']:
            self.fetch(data['link']['next'], debug)

    def save_listing(self, listing_data: dict):
        """
        Save a listing.
        :param listing_data:
        :return: (TNZListing, bool)
        """
        flag = self.UNCHANGED
        listing_sorted_data = {
            'name': listing_data['nameoflisting'],
            'modified_date': timezone.make_aware(datetime.datetime.strptime(
                listing_data['modified_date'], '%B, %d %Y %X')
            ),
            'regionname': listing_data['regionname'],
            'unique_id': listing_data['unique_id'],
            'market': listing_data['market'],
            'listing_description': listing_data['listing_description'],
            'listing_summary': listing_data['listing_summary'],
            'latitude': self.convert_latlng(listing_data['latitude']),
            'longitude': self.convert_latlng(listing_data['longitude']),
            'business_type': listing_data['business_type'],
            'minimum_age': listing_data['minimum_age'],
            'max_capacity': str(listing_data['max_capacity']),
            'website_link': listing_data['website_link'],
            'booking_link': listing_data['booking_link'],
            'phone': listing_data['phone'],
            'mobile': listing_data['mobile'],
            'email': listing_data['email'],
            'operational_hours': listing_data['operational_hours'],
            'street': listing_data['street'],
            'suburb': listing_data['suburb'],
            'city': listing_data['city'],
            'postcode': str(listing_data['postcode']),
            'proximity_to_town': listing_data['proximity_to_town'],
            'proximity_to_airport': listing_data['proximity_to_airport'],
            'freephone': listing_data['freephone'],
            'listing_types': listing_data['listing_types'],
            'booking_email': listing_data['booking_email'],
            'cancellation_policy': listing_data['cancellation_policy'],
            'parking': listing_data['parking'],
        }
        try:
            listing = TNZListing.objects.get(unique_id=listing_sorted_data['unique_id'])
        except TNZListing.DoesNotExist:
            flag = self.IMPORTED
            listing = TNZListing(**listing_sorted_data)
        else:
            for key, value in listing_sorted_data.items():
                if getattr(listing, key) != value:
                    setattr(listing, key, value)
                    flag = self.UPDATED

        # Save main image and logo image
        for image_type in ('main', 'logo'):
            image_data = listing_data['assets'].get(image_type)
            if image_data is not None:
                for key, value in image_data.items():
                    result = self.save_image(value)
                    setattr(listing, image_type + '_image', result[0])
                    if flag != self.IMPORTED and result[1] != self.UNCHANGED:
                        flag = self.UPDATED

        listing.save()

        # Save gallery images
        gallery_images_data = listing_data['assets'].get('gallery')
        if gallery_images_data is not None:
            for key, value in gallery_images_data.items():
                result = self.save_image(value)
                listing.gallery_images.add(result[0])
                if flag != self.IMPORTED and result[1] != self.UNCHANGED:
                    flag = self.UPDATED

        tags_data = listing_data['tags']
        if tags_data:
            for tag_name in tags_data:
                # There can be more than 1 tags having the same label.
                tags = TNZTag.objects.filter(label=tag_name)
                if tags.exists():
                    for tag in tags:
                        listing.tags.add(tag)

        listing.save()

        return listing, flag

    def save_image(self, image_data):
        """
        Save a TNZImage. It will also save the related TNZImageInstance.
        It will check image instance 'format' key as the unique key for the image.
        :param image_data:
        :return (TNZImage bool):
        """
        flag = self.UNCHANGED
        image_sorted_data = {
            'o_id': image_data['o_id'],
            'unique_id': image_data['unique_id'],
            'type_o_id': image_data['type_o_id'],
            'description': image_data['description'],
            'label': image_data['label'],
            'width': image_data['width'],
            'height': image_data['height'],
            'order': image_data.get('order'),
            'market': image_data['market'],
            'latitude': self.convert_latlng(image_data['latitude']),
            'longitude': self.convert_latlng(image_data['longitude']),
            'asset_type': image_data['asset_type'],
            'credit': image_data['credit'],
            'exists': image_data['exists'],
            'caption': image_data['caption'],
            'url': image_data['url'],
        }
        try:
            image = TNZImage.objects.get(unique_id=image_data['unique_id'])
        except TNZImage.DoesNotExist:
            image = TNZImage(**image_sorted_data)
            flag = self.IMPORTED
        else:
            for key, value in image_sorted_data.items():
                if getattr(image, key) != value:
                    setattr(image, key, value)
                    flag = self.UPDATED

        image.save()

        for instance_data in image_data['instances']:
            instance_sorted_data = {
                'provider_label': instance_data['provider_label'],
                'format': instance_data['format'],
                'width': instance_data['width'],
                'height': instance_data['height'],
                'url': instance_data['url'],
            }
            try:
                instance = image.instances.get(format=instance_sorted_data['format'])
            except TNZImageInstance.DoesNotExist:
                instance = TNZImageInstance(**instance_sorted_data)
            else:
                instance.image = image
                for key, value in instance_sorted_data.items():
                    if getattr(instance, key) != value:
                        setattr(instance, key, value)
                        if flag != self.IMPORTED:
                            flag = self.UPDATED
            instance.image = image
            instance.save()

        return image, flag

    @staticmethod
    def convert_latlng(value):
        if not value:
            return float(0)
        else:
            return float(value)
