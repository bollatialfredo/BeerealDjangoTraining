from django.core.management.base import BaseCommand, CommandError
from shortener.models import beereal_trainingURL

class Command(BaseCommand):
    help = 'refreshes all beereal_trainingURL shortcodes'
    def add_arguments(self, parser):
        parser.add_argument('items', type=int)

    def handle(self, *args, **options):
        return beereal_trainingURL.objects.refresh_shortcodes(items=options['items'])
