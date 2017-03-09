from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from wagtail.contrib.modeladmin.helpers import PermissionHelper

from .models import ContactRecord


class ContactRecordPermissionHelper(PermissionHelper):
    def user_can_create(self, user):
        return False


class ContactRecordAdmin(ModelAdmin):
    model = ContactRecord
    menu_label = 'Contact Records'
    menu_icon = 'mail'
    list_display = ('name', 'email', 'subject', 'created')
    list_filter = ('name', 'email')
    search_fields = ('name', 'email', 'subject', 'message')
    permission_helper_class = ContactRecordPermissionHelper

modeladmin_register(ContactRecordAdmin)
