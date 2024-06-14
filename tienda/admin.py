from django.contrib import admin
from .models import CategoriaProducto, Producto


class CategoriaProductoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")
# Register your models here.
admin.site.register(Producto,ProductoAdmin)
admin.site.register(CategoriaProducto,CategoriaProductoAdmin)
