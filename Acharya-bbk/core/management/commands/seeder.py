from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = "Run all seeders"

    def handle(self, *args, **kwargs):
        call_command("seed_groups")
        self.stdout.write(self.style.SUCCESS("All seeders executed successfully"))
