import random
import string

def code_generator(size=6, char=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(char) for _ in range(size))

def create_shotcode(instance, size=6):
    new_code = code_generator(size=size)
    klass = instance.__class__
    qs_exists = klass.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shotcode(size=size)
    return new_code
