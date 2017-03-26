from rest_framework import serializers

from listings.models import TNZListing, TNZImage


class TNZImageField(serializers.RelatedField):
    """
    Get resized image information.
    """
    def to_representation(self, value):
        if isinstance(value, TNZImage) and value.file:
            return {
                'description': value.description,
                'label': value.label,
                'small': value.get_thumbnail('250x300').url,
                'large': value.get_thumbnail('1280x500').url
            }
        return None

    def to_internal_value(self, data):
        return self.to_representation()


class ListingSerializer(serializers.HyperlinkedModelSerializer):
    """
    The Listing serializer.
    """
    main_image = TNZImageField(many=False, read_only=True)
    logo_image = TNZImageField(many=False, read_only=True)
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
