from rest_framework import serializers

from listings.models import TNZListing, TNZImage


class TNZImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TNZImage
        fields = ('description', 'label', 'caption', 'file')


class ListingSerializer(serializers.HyperlinkedModelSerializer):
    main_image = TNZImageSerializer(many=False, read_only=True)
    logo_image = TNZImageSerializer(many=False, read_only=True)
    # gallery_images = TNZImageSerializer(many=True, read_only=True)

    class Meta:
        model = TNZListing
        fields = (
            'name',
            'unique_id',
            'market',
            'listing_summary',
            'listing_description',
            'regionname',
            'business_type',
            'latitude',
            'longitude',
            'main_image',
            'logo_image',
            # 'gallery_images',
        )
