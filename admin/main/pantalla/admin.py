from django.contrib import admin
from .models import *
from django.forms import widgets
from django.contrib.postgres.fields import JSONField 

class MultiDBModelAdmin(admin.ModelAdmin):
    # A handy constant for the name of the alternate database.
    using = 'default'

 
    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'postgres' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'postgres' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'postgres' database.
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'postgres' database.
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'postgres' database.
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)


class MultiDBTabularInline(admin.TabularInline):
    using = 'postgres'

    def get_queryset(self, request):
        # Tell Django to look for inline objects on the 'postgres' database.
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'postgres' database.
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'postgres' database.
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)


class CatalogueDetailInline(MultiDBTabularInline):
    model = CatalogueDetail


class CatalogueAdmin(MultiDBModelAdmin):
    inlines = [CatalogueDetailInline]


class ExperienceDetailInline(MultiDBTabularInline):
    model = ExperienceDetail


class ExperienceAdmin(MultiDBModelAdmin):
    inlines = [ExperienceDetailInline]


admin.site.register(Experience, ExperienceAdmin)

admin.site.register(Catalogue, CatalogueAdmin)
