from django.db import models
from django.utils.safestring import mark_safe


class Drawing(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    image = models.ImageField(upload_to='online_store', null=True, blank=True)

    def image_tag(self):
        return mark_safe(f'<img src={self.image.url} style="max-height: 200px;" />')

    image_tag.allow_tags = True
    image_tag.short_description = "Изображение"