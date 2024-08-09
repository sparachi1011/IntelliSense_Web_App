# your_app/management/commands/copy_data.py
# from django.core.management.base import BaseCommand
# from authentication.models import SourceModel, TargetModel

# class Command(BaseCommand):
#     help = 'Copy data from SourceModel in the source database to TargetModel in the target database'

#     def handle(self, *args, **kwargs):
#         # Fetch all records from the source table in the 'default' database
#         source_data = SourceModel.objects.using('secondary').all()

#         # Iterate and copy data to the target table in the 'secondary' database
#         for record in source_data:
#             TargetModel.objects.using('default').create(
#                 field1=record.field1,
#                 field2=record.field2,
#             )

#         self.stdout.write(self.style.SUCCESS('Data copied successfully!'))


from django.db import connection
db = connection.creation.create_test_db(settings.configure()"db.sqlite3")
print(db)