from django.db import models
import transliterate


# Create your models here.
class Ghost(models.Model):
    """Модель призрака"""
    name = models.CharField(max_length=255, verbose_name='Название', unique=True)
    slug = models.SlugField(max_length=255, verbose_name='Slug',
                            unique=True, blank=True, null=True)
    properties = models.TextField(verbose_name='Свойства')
    evidences = models.ManyToManyField('Evidence', verbose_name='Улики', related_name='ghosts', null=True, blank=True)

    class Meta:
        verbose_name = 'Призрак'
        verbose_name_plural = 'Призраки'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = transliterate.slugify(self.name)
        super().save(*args, **kwargs)


class Evidence(models.Model):
    """Модель улик"""
    name = models.CharField(max_length=255, verbose_name='Название', unique=True)
    properties = models.TextField(verbose_name='Свойства')
    slug = models.SlugField(max_length=255, verbose_name='Slug', unique=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Улика'
        verbose_name_plural = "Улики"
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.title:
            self.slug = transliterate.slugify(self.name)
        super().save(*args, **kwargs)
