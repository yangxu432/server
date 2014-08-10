from django.contrib import admin
from fvcom.models import *
# Register your models here.
class VariableInline(admin.TabularInline):
    model = Variable

class TypeInline(admin.TabularInline):
    model = Type

class ValueInline(admin.TabularInline):
    model = Value

class SationLinkInline(admin.TabularInline):
    model = Station

class StationIndexAdmin(admin.ModelAdmin):
    inlines = [SationLinkInline,]

admin.site.register(Station)
admin.site.register(StationIndex, StationIndexAdmin)

class ModelAdmin(admin.ModelAdmin):
    inlines = [VariableInline,]

admin.site.register(Model, ModelAdmin)

class VariableAdmin(admin.ModelAdmin):
    inlines = [TypeInline,]
    list_filter = ('model__display_title',)
admin.site.register(Variable, VariableAdmin)

class TypeAdmin(admin.ModelAdmin):
    inlines = [ValueInline,]
    list_filter = ('variable__model__display_title','variable',)

admin.site.register(Type, TypeAdmin)

