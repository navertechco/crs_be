from django.contrib import admin
# from django_monaco_editor.widgets import AdminMonacoEditorWidget
from django.db import models
# from codemirror2.widgets import CodeMirrorEditor
# from codemirror import CodeMirrorTextarea
# Register your models here.
from .models import *

# codemirror_widget = CodeMirrorTextarea(
#     mode="javascript",
#     theme="night",
#     config={
#         'spellcheck': True,
#         'fixedGutter': True,
#         'lineNumbers': True,

#     },
# )


class AnswerAdmin(admin.ModelAdmin):
    # A handy constant for the name of the alternate database.
    using = 'postgres'
    # formfield_overrides = {
    #     models.TextField: {'widget': codemirror_widget}
    # }

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'mssql' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'mssql' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'mssql' database.
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'mssql' database.
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'mssql' database.
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)

    # list_filter = ('id_answer', 'answer_text', 'id_question_fk')
    list_display = ('id_answer', 'answer_text', 'id_question_fk')
    # search_fields = ('id_answer', 'answer_text', 'id_question_fk')

    pass


admin.site.register(Answer, AnswerAdmin)


class DetailCatalogueAdmin(admin.ModelAdmin):
    # A handy constant for the name of the alternate database.
    using = 'postgres'
    # formfield_overrides = {
    #     models.TextField: {'widget': codemirror_widget}
    # }

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'mssql' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'mssql' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'mssql' database.
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'mssql' database.
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'mssql' database.
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)

    list_filter = ( 'id_detail_catalogue','description')
    list_display = ( 'id_detail_catalogue','description')
    search_fields = ( 'id_detail_catalogue','description')

    pass


admin.site.register(DetailCatalogue, DetailCatalogueAdmin)


class GameLogAdmin(admin.ModelAdmin):
    # A handy constant for the name of the alternate database.
    using = 'postgres'
    # formfield_overrides = {
    #     models.TextField: {'widget': codemirror_widget}
    # }

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'mssql' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'mssql' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'mssql' database.
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'mssql' database.
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'mssql' database.
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)

    # list_filter = ('window', 'type', 'name')
    # list_display = ('window', 'type', 'name')
    # search_fields = ('window', 'type', 'name','params')

    pass


admin.site.register(GameLog, GameLogAdmin)


class GamerAdmin(admin.ModelAdmin):
    # A handy constant for the name of the alternate database.
    using = 'postgres'
    # formfield_overrides = {
    #     models.TextField: {'widget': codemirror_widget}
    # }

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'mssql' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'mssql' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'mssql' database.
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'mssql' database.
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'mssql' database.
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)

    list_filter = ('identification', 'username')
    list_display = ('identification', 'username')
    search_fields = ('identification', 'username')

    pass


admin.site.register(Gamer, GamerAdmin)


class GamerTournamentAdmin(admin.ModelAdmin):
    # A handy constant for the name of the alternate database.
    using = 'postgres'
    # formfield_overrides = {
    #     models.TextField: {'widget': codemirror_widget}
    # }

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'mssql' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'mssql' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'mssql' database.
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'mssql' database.
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'mssql' database.
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)

    # list_filter = ('window', 'type', 'name')
    # list_display = ('window', 'type', 'name')
    # search_fields = ('window', 'type', 'name','params')

    pass


admin.site.register(GamerTournament, GamerTournamentAdmin)


class MasterCatalogueAdmin(admin.ModelAdmin):
    # A handy constant for the name of the alternate database.
    using = 'postgres'
    # formfield_overrides = {
    #     models.TextField: {'widget': codemirror_widget}
    # }

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'mssql' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'mssql' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'mssql' database.
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'mssql' database.
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'mssql' database.
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)

    # list_filter = ('window', 'type', 'name')
    # list_display = ('window', 'type', 'name')
    # search_fields = ('window', 'type', 'name','params')

    pass


admin.site.register(MasterCatalogue, MasterCatalogueAdmin)


class PurchasesAdmin(admin.ModelAdmin):
    # A handy constant for the name of the alternate database.
    using = 'postgres'
    # formfield_overrides = {
    #     models.TextField: {'widget': codemirror_widget}
    # }

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'mssql' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'mssql' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'mssql' database.
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'mssql' database.
        if db_field.name == "payment_type_fk":
            kwargs["queryset"] = DetailCatalogue.objects.filter(description__in=['efectivo'])
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'mssql' database.
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)

    list_filter = ( 'purchase_date', 'num_credits')
    list_display = ( 'purchase_date', 'num_credits')
    search_fields = ( 'purchase_date', 'num_credits' )

    pass


admin.site.register(Purchases, PurchasesAdmin)


class QuestionAdmin(admin.ModelAdmin):
    # A handy constant for the name of the alternate database.
    using = 'postgres'
    # formfield_overrides = {
    #     models.TextField: {'widget': codemirror_widget}
    # }

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'mssql' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'mssql' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'mssql' database.
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'mssql' database.
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'mssql' database.
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)

    list_filter = ('id_question', 'question_text')
    list_display = ('id_question', 'question_text')
    search_fields = ('id_question', 'question_text' )

    pass


admin.site.register(Question, QuestionAdmin)


class TournamentAdmin(admin.ModelAdmin):
    # A handy constant for the name of the alternate database.
    using = 'postgres'
    # formfield_overrides = {
    #     models.TextField: {'widget': codemirror_widget}
    # }

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'mssql' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'mssql' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'mssql' database.
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'mssql' database.
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'mssql' database.
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)

    # list_filter = ('id_tournament',)
    list_display = ('id_tournament',)
    # search_fields = ('id_tournament',)

    pass


admin.site.register(Tournament, TournamentAdmin)


class TournamentSubjectAdmin(admin.ModelAdmin):
    # A handy constant for the name of the alternate database.
    using = 'postgres'
    # formfield_overrides = {
    #     models.TextField: {'widget': codemirror_widget}
    # }

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'mssql' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'mssql' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'mssql' database.
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'mssql' database.
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'mssql' database.
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)

    list_filter = ('id_tournament_subject', 'description')
    list_display = ('id_tournament_subject', 'description')
    search_fields = ('id_tournament_subject', 'description')

    pass


admin.site.register(TournamentSubject, TournamentSubjectAdmin)


class WinnerAdmin(admin.ModelAdmin):
    # A handy constant for the name of the alternate database.
    using = 'postgres'
    # formfield_overrides = {
    #     models.TextField: {'widget': codemirror_widget}
    # }

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'mssql' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'mssql' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'mssql' database.
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'mssql' database.
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'mssql' database.
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)

    # list_filter = ('position',)
    # list_display = ('position',)
    # search_fields = ('position',)

    pass


admin.site.register(Winner, WinnerAdmin)
