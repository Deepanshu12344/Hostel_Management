# from django.apps import AppConfig

# class FirstappConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'firstapp'

#     def ready(self):
#         import firstapp.signals
    

#  USED FOR TRIGGER 

from django.apps import AppConfig
from django.db import connection

class FirstappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'firstapp'

    def ready(self):
        # Check if the trigger already exists before running migrations
        with connection.cursor() as cursor:
            cursor.execute("SHOW TRIGGERS LIKE 'after_hostelite_delete';")
            trigger_exists = cursor.fetchone()

            if not trigger_exists:
                import firstapp.signals
