import random
import string
from django.conf import settings

SHORTCODE_MIN = getattr(settings, 'SHORTCODE_MIN', 6)

def code_generator(size=SHORTCODE_MIN, char=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(char) for _ in range(size))

def create_shotcode(instance, size=SHORTCODE_MIN):
    new_code = code_generator(size=size)
    klass = instance.__class__
    qs_exists = klass.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shotcode(size=size)
    return new_code
