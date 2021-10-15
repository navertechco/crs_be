from django.contrib import admin
# from django.contrib.postgres import fields # if django < 3.1
from django.db import models
from django_json_widget.widgets import JSONEditorWidget
from .models import *


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    formfield_overrides = { 
        models.TextField: {'widget': JSONEditorWidget},
    }
@admin.register(Catalogue)
class CatalogueAdmin(admin.ModelAdmin):
    formfield_overrides = { 
        models.TextField: {'widget': JSONEditorWidget},
    }
@admin.register(CatalogueDetail)
class CatalogueDetailAdmin(admin.ModelAdmin):
    formfield_overrides = { 
        models.TextField: {'widget': JSONEditorWidget},
    }
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    formfield_overrides = { 
        models.TextField: {'widget': JSONEditorWidget},
    }
@admin.register(ClientType)
class ClientTypeAdmin(admin.ModelAdmin):
    formfield_overrides = { 
        models.TextField: {'widget': JSONEditorWidget},
    }
@admin.register(Delimiter)
class DelimiterAdmin(admin.ModelAdmin):
    formfield_overrides = { 
        models.TextField: {'widget': JSONEditorWidget},
    }
@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    formfield_overrides = { 
        models.TextField: {'widget': JSONEditorWidget},
    }
@admin.register(DestinationService)
class DestinationServiceAdmin(admin.ModelAdmin):
    formfield_overrides = { 
        models.TextField: {'widget': JSONEditorWidget},
    }
@admin.register(KeyActivity)
class KeyActivityAdmin(admin.ModelAdmin):
    formfield_overrides = { 
        models.TextField: {'widget': JSONEditorWidget},
    }
@admin.register(LegalClientType)
class LegalClientTypeAdmin(admin.ModelAdmin):
    formfield_overrides = { 
        models.TextField: {'widget': JSONEditorWidget},
    }
@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    formfield_overrides = { 
        models.TextField: {'widget': JSONEditorWidget},
    }
@admin.register(MediaType)
class MediaTypeAdmin(admin.ModelAdmin):
    formfield_overrides = { 
        models.TextField: {'widget': JSONEditorWidget},
    }
@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    formfield_overrides = { 
        models.TextField: {'widget': JSONEditorWidget},
    }
@admin.register(PlaylistState)
class PlaylistStateAdmin(admin.ModelAdmin):
    formfield_overrides = { 
        models.TextField: {'widget': JSONEditorWidget},
    }
@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    formfield_overrides = { 
        models.TextField: {'widget': JSONEditorWidget},
    }
@admin.register(PromoDetail)
class PromoDetailAdmin(admin.ModelAdmin):
    formfield_overrides = { 
        models.TextField: {'widget': JSONEditorWidget},
    }
@admin.register(Purpouse)
class PurpouseAdmin(admin.ModelAdmin):
    formfield_overrides = { 
        models.TextField: {'widget': JSONEditorWidget},
    }
@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    formfield_overrides = { 
        models.TextField: {'widget': JSONEditorWidget},
    }
@admin.register(QuoteDetail)
class QuoteDetailAdmin(admin.ModelAdmin):
    formfield_overrides = { 
        models.TextField: {'widget': JSONEditorWidget},
    }
@admin.register(QuoteState)
class QuoteStateAdmin(admin.ModelAdmin):
    formfield_overrides = { 
        models.TextField: {'widget': JSONEditorWidget},
    }
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    formfield_overrides = { 
        models.TextField: {'widget': JSONEditorWidget},
    }
@admin.register(ServiceDetail)
class ServiceDetailAdmin(admin.ModelAdmin):
    formfield_overrides = { 
        models.TextField: {'widget': JSONEditorWidget},
    }
@admin.register(ServiceSupplier)
class ServiceSupplierAdmin(admin.ModelAdmin):
    formfield_overrides = { 
        models.TextField: {'widget': JSONEditorWidget},
    }
@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    formfield_overrides = { 
        models.TextField: {'widget': JSONEditorWidget},
    }
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    formfield_overrides = { 
        models.TextField: {'widget': JSONEditorWidget},
    }
@admin.register(SupplierType)
class SupplierTypeAdmin(admin.ModelAdmin):
    formfield_overrides = { 
        models.TextField: {'widget': JSONEditorWidget},
    }
@admin.register(TravelRitm)
class TravelRitmAdmin(admin.ModelAdmin):
    formfield_overrides = { 
        models.TextField: {'widget': JSONEditorWidget},
    }
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    formfield_overrides = { 
        models.TextField: {'widget': JSONEditorWidget},
    }
