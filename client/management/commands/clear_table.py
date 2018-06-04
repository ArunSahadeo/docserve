#!/usr/bin/env python3

from django.core.management.base import BaseCommand, CommandError
from client.models import *

class Command(BaseCommand):
    help = 'Clears all rows from the specified table.'

    def add_arguments(self, parser):
        parser.add_argument('table', nargs=1, type=str)

    def handle(self, *args, **options):
        table = str(options['table'][0]).lower().capitalize()

        if table == 'Library':
            try:
                Library.objects.all().delete()
            except Library.DoesNotExist:
                raise CommandError('The table "%s" does not exist' % str(options['table']))
        elif table == 'Version':
            try:
                Version.objects.all().delete()
            except Version.DoesNotExist:
                raise CommandError('The table "%s" does not exist' % str(options['table']))
        elif table == 'Resource':
            try:
                Resource.objects.all().delete()
            except Resource.DoesNotExist:
                raise CommandError('The table "%s" does not exist' % str(options['table']))
        else:
            raise CommandError('The table "%s" does not exist' % str(options['table']))

        self.stdout.write(self.style.SUCCESS('All rows in table "%s" were cleared' % str(options['table'])))
