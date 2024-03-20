from django.core.management.base import BaseCommand, CommandError
from map.models import Location

# Define a custom command to populate the database with predefined locations
class Command(BaseCommand):
    help = 'Populates the database with predefined locations'

    def handle(self, *args, **options):
        locations = [
            {'location_id': '1', 'name': 'CREWW Building'},
            {'location_id': '2', 'name': 'Car Park B'},
            {'location_id': '3', 'name': 'Greenhouse'},
            {'location_id': '4', 'name': 'Reed Pond'},
            {'location_id': '5', 'name': 'East Park'},
            {'location_id': '6', 'name': 'Wellbeing Services Facility'},
            {'location_id': '7', 'name': 'Taddiforde Valley'},
            {'location_id': '8', 'name': 'Pine Tree Belt'},
            {'location_id': '9', 'name': 'Field above Car Park B'},
            {'location_id': '10', 'name': 'Laver Pond'},
            {'location_id': '11', 'name': 'Plantation'},
            {'location_id': '12', 'name': 'Poole Gate'},
        ]

        for loc in locations:
            Location.objects.get_or_create(
                location_id=loc['location_id'],
                defaults={'name': loc['name']}
            )
        
        self.stdout.write(self.style.SUCCESS('Successfully populated locations'))