from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = "Seeds default groups with permissions"

    def handle(self, *args, **kwargs):
        roles = ["Parent", "Teacher", "Staff Admin", "Student"]
        for role in roles:
            group, created = Group.objects.get_or_create(name=role)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Role '{role}' created"))
            else:
                self.stdout.write(self.style.WARNING(f"Role '{role}' already exists"))
