# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from galleries.models import Gallery
from galleries.forms import GalleryForm

"""
Listagem da galeria de imagens
"""
def index(request):
    galleries = Gallery.objects.all().order_by('-id')
    context = {'galleries': galleries}
    return render(request, 'galleries/index.html', context)

"""
Detalhes da galeria corrente
"""
def detail(request, gallery_id):
    gallery = get_object_or_404(Gallery, pk=gallery_id)
    context = {'gallery': gallery}
    return render(request, 'galleries/detail.html', context)