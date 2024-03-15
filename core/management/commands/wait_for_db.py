import time

from django.core.management import BaseCommand
from django.db.utils import OperationalError
from MySQLdb import OperationalError as MySQLOperationalError


class Command(BaseCommand):
    """Custom django command to wait for the database to be ready"""

    def handle(self, *args, **options):
        """
        The entry point that is called when the command is run
        Args:
            *args:
            **options:

        Returns:

        """
        self.stdout.write("Waiting for MySQL database ... ")
        db_conn = False
        while not db_conn:
            try:
                self.check(databases=["default"])
                db_conn = True
            except (MySQLOperationalError, OperationalError) as e:
                self.stdout.write("Database Unavailable. Waiting 1 second")
                self.stdout.write(self.style.SUCCESS(str(e)))
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database Available for connections"))
