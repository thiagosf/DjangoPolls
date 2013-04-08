from django.db import models

# Create your models here.

class Gallery(models.Model):
    title = models.CharField(verbose_name='Titulo da imagem', max_length=250)
    image = models.ImageField(verbose_name='Imagem', upload_to='%Y/%m/%d/')

    @property
    def filename(self):
        return self.image.name.rsplit('/', 1)[-1]

    def __unicode__(self):
        return self.title

    def image_img(self):
        if self.image:
            return u'<a href="%s" rel="lightbox"><img src="%s" width="50" /></a>' % (self.image.url, self.image.url)
        else:
            return '(Sem imagem)'

    image_img.short_description = 'Thumb'
    image_img.allow_tags = True

    class Meta:
        verbose_name = 'galeria'
        verbose_name_plural = 'galerias'