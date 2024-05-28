import json
from config.settings.base import BASE_DIR
from django.core.management.base import BaseCommand
from common.models import Country, Region

class Command(BaseCommand):
    help = "load regions of Uzbekistan"

    def handle(self, *args, **options):
        try:
            uzbekistan = Country.objects.get(code = 'UZ')
            with open(str(BASE_DIR) + '/data/uz_regions.json') as file:
                regions = json.load(file)
                for i in regions:
                    Region.objects.get_or_create(name = i.get('name_en').split()[0], country_name=uzbekistan)
            self.stdout.write(self.style.SUCCESS("Regions loaded successfully"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error {e}"))