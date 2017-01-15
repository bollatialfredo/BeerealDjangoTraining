from django.conf import settings
from django.db import models
from .utils import code_generator, create_shotcode

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

class beereal_trainingURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(beereal_trainingURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active = True)
        return qs

    def refresh_shortcodes(self, items=None):
        qs = beereal_trainingURL.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int) and items > 0:
            qs = qs.order_by('id')[:items]
        new_codes = 0
        for q in qs:
            q.shortcode = create_shotcode(q)
            print(q.id)
            q.save()
            new_codes += 1
        return 'New codes created: {i}'.format(i=new_codes)


class beereal_trainingURL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    updated = models.DateTimeField(auto_now = True)
    timestamp = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default = True)

    objects = beereal_trainingURLManager()

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == '':
            self.shortcode = create_shotcode(self)
        super(beereal_trainingURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
    def __unicode__(self):
        return str(self.url)


"""

siempre cuando se modifica algo del modelo correr los siguientes comandos

--> python manage.py makemigations
--> python manage.py migrate

de esta forma se mantiene alineados los modelos con la BBDD

"""
