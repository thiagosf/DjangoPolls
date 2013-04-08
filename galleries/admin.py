from django.contrib import admin
from galleries.models import Gallery

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image_img')

admin.site.register(Gallery, GalleryAdmin)