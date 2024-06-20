from django.core.management.base import BaseCommand
import subprocess


class Command(BaseCommand):
    help = "Launch module 1"

    # def add_arguments(self, parser):
    #     parser.add_argument("poll_ids", nargs="+", type=int)

    def handle(self, *args, **options):
        # subprocess.call(" python mon_module.py")
        print("Bonjour")
