from django.contrib import admin
from django.contrib.postgres import fields  # if django < 3.1
from django.db import models
from django_json_widget.widgets import JSONEditorWidget
from src.models.models import *
from django.apps import apps
import src.models.models as modelmodule


modellist = (list(modelmodule.__dict__))


class ModelAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if request.user.groups.filter(name='travelexpert').exists():
            if self.model._meta.permissions is not None and len(self.model._meta.permissions) > 0 and self.model._meta.permissions[0][0] == 'add_item':
                return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if request.user.groups.filter(name='travelexpert').exists():
            if self.model._meta.permissions is not None and len(self.model._meta.permissions) > 0 and self.model._meta.permissions[1][0] == 'change_item':
                return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if request.user.groups.filter(name='travelexpert').exists():
            if self.model._meta.permissions is not None and len(self.model._meta.permissions) > 0 and self.model._meta.permissions[2][0] == 'delete_item':
                return True
        return False

    def get_fields(self, request, obj=None):
        if not request.user.is_superuser and request.user.has_perm('items.read_item'):
            return [f.name for f in self.model._meta.fields]
        return super(ModelAdmin, self).get_fields(
            request, obj=obj
        )


class ListAdminMixin(object):
    def __init__(self, model, admin_site):
        # self.list_display = [field.description for field in model._meta.fields]
        super(ListAdminMixin, self).__init__(model, admin_site)
    formfield_overrides = {
        models.TextField: {'widget': JSONEditorWidget},
    }

modellist = apps.get_models()
for model in modellist:
    admin_class = type('AdminClass', (ListAdminMixin, admin.ModelAdmin, ), {})
    admin_class_perm = type('AdminClass', (admin_class, ModelAdmin, ), {})

    try:
        admin.site.register(model, admin_class_perm)
    except Exception as e:
        pass

# @admin.register(Budget)
# class BudgetAdmin(admin.ModelAdmin):
#     list_display = ('description',)
#     formfield_overrides = {
#         models.TextField: {'widget': JSONEditorWidget},
#     }

# @admin.register(Client)
# class ClientAdmin(admin.ModelAdmin):
#     list_display = ('name_contact',)
#     formfield_overrides = {
#         models.TextField: {'widget': JSONEditorWidget},
#     }

# @admin.register(Origin)
# class OriginAdmin(admin.ModelAdmin):
#     list_display = ('description',)
#     formfield_overrides = {
#         models.TextField: {'widget': JSONEditorWidget},
#     }
# @admin.register(ClientType)
# class ClientTypeAdmin(admin.ModelAdmin):
#     list_display = ('description',)
#     formfield_overrides = {
#         models.TextField: {'widget': JSONEditorWidget},
#     }
# @admin.register(Agent)
# class AgentAdmin(admin.ModelAdmin):
#     list_display = ('description',)
#     formfield_overrides = {
#         models.TextField: {'widget': JSONEditorWidget},
#     }
# @admin.register(TravelExpert)
# class TravelExpertAdmin(admin.ModelAdmin):
#     list_display = ('description',)
#     formfield_overrides = {
#         models.TextField: {'widget': JSONEditorWidget},
#     }

# @admin.register(Itinerary)
# class ItineraryAdmin(admin.ModelAdmin):
#     list_display = ('itinerary_id',)
#     formfield_overrides = {
#         models.TextField: {'widget': JSONEditorWidget},
#     }
# @admin.register(AgeFriendlyRange)
# class AgeFriendlyRangeAdmin(admin.ModelAdmin):
#     list_display = ('description',)
#     formfield_overrides = {
#         models.TextField: {'widget': JSONEditorWidget},
#     }
# @admin.register(Delimiter)
# class DelimiterAdmin(admin.ModelAdmin):
#     list_display = ('description',)
#     formfield_overrides = {
#         models.TextField: {'widget': JSONEditorWidget},
#     }
# @admin.register(Destination)
# class DestinationAdmin(admin.ModelAdmin):
#     list_display = ('description',)
#     formfield_overrides = {
#         models.TextField: {'widget': JSONEditorWidget},
#     }
# @admin.register(KeyActivity)
# class KeyActivityAdmin(admin.ModelAdmin):
#     list_display = ('description',)
#     formfield_overrides = {
#         models.TextField: {'widget': JSONEditorWidget},
#     }
# @admin.register(LegalClientType)
# class LegalClientTypeAdmin(admin.ModelAdmin):
#     list_display = ('description',)
#     formfield_overrides = {
#         models.TextField: {'widget': JSONEditorWidget},
#     }
# @admin.register(Media)
# class MediaAdmin(admin.ModelAdmin):
#     list_display = ('description',)
#     formfield_overrides = {
#         models.TextField: {'widget': JSONEditorWidget},
#     }
# @admin.register(MediaType)
# class MediaTypeAdmin(admin.ModelAdmin):
#     list_display = ('description',)
#     formfield_overrides = {
#         models.TextField: {'widget': JSONEditorWidget},
#     }
# @admin.register(Playlist)
# class PlaylistAdmin(admin.ModelAdmin):
#     list_display = ('description',)
#     formfield_overrides = {
#         models.TextField: {'widget': JSONEditorWidget},
#     }

# @admin.register(Promo)
# class PromoAdmin(admin.ModelAdmin):
#     list_display = ('description',)
#     formfield_overrides = {
#         models.TextField: {'widget': JSONEditorWidget},
#     }
# @admin.register(Service)
# class ServiceAdmin(admin.ModelAdmin):
#     list_display = ('description',)
#     formfield_overrides = {
#         models.TextField: {'widget': JSONEditorWidget},
#     }

# @admin.register(ServiceType)
# class ServiceTypeAdmin(admin.ModelAdmin):
#     list_display = ('description',)
#     formfield_overrides = {
#         models.TextField: {'widget': JSONEditorWidget},
#     }
# @admin.register(Supplier)
# class SupplierAdmin(admin.ModelAdmin):
#     list_display = ('description',)
#     formfield_overrides = {
#         models.TextField: {'widget': JSONEditorWidget},
#     }
# @admin.register(SupplierType)
# class SupplierTypeAdmin(admin.ModelAdmin):
#     list_display = ('description',)
#     formfield_overrides = {
#         models.TextField: {'widget': JSONEditorWidget},
#     }

# @admin.register(PaymentType)
# class PaymentTypeAdmin(admin.ModelAdmin):
#     list_display = ('description',)
#     formfield_overrides = {
#         models.TextField: {'widget': JSONEditorWidget},
#     }


# @admin.register(City)
# class CityAdmin(admin.ModelAdmin):
#     list_display = ('description',)
#     formfield_overrides = {
#         models.TextField: {'widget': JSONEditorWidget},
#     }
# @admin.register(SupplierRule)
# class SupplierRuleAdmin(admin.ModelAdmin):
#     list_display = ('description',)
#     formfield_overrides = {
#         models.TextField: {'widget': JSONEditorWidget},
#     }
# @admin.register(TravelRitm)
# class TravelRitmAdmin(admin.ModelAdmin):
#     list_display = ('description',)
#     formfield_overrides = {
#         models.TextField: {'widget': JSONEditorWidget},
#     }
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('description',)
#     formfield_overrides = {
#         models.TextField: {'widget': JSONEditorWidget},
#     }
