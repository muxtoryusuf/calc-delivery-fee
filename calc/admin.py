from django.contrib import admin
from . models import Region, Dimension, Tariff
# Register your models here.


@admin.register(Dimension)
class DimensionAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "width",
        "length",
        "height",
        "cube",
    ]

    list_display_links = ('width', 'length')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj=None, **kwargs)
        form.base_fields["cube"].disabled = True
        return form


admin.site.register(Region)

admin.site.register(Tariff)
