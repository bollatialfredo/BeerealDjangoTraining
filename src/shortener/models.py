from django.db import models

class beereal_trainingURL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=15, unique=True)
    updated = models.DateTimeField(auto_now = True)
    timestamp = models.DateTimeField(auto_now_add = True)


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
