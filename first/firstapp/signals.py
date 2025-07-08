# from django.db.backends.signals import connection_created
# from django.dispatch import receiver

# @receiver(connection_created)
# def activate_foreign_keys(sender, connection, **kwargs):
#     with connection.cursor() as cursor:
#         with open('path/to/your/triggers.sql', 'r') as f:
#             cursor.execute(f.read())


# signals.py in your firstapp

# from django.db.backends.signals import connection_created
# from django.dispatch import receiver
# import os

# @receiver(connection_created)
# def activate_foreign_keys(sender, connection, **kwargs):
#     script_path = os.path.join(os.path.dirname(__file__), 'triggers.sql')
#     with connection.cursor() as cursor:
#         with open(script_path, 'r') as f:
#             cursor.execute(f.read())









# from django.db.backends.signals import connection_created
# from django.dispatch import receiver
# import os
# from django.db import connection

# @receiver(connection_created)
# def activate_foreign_keys(sender, connection, **kwargs):
#     script_path = os.path.join(os.path.dirname(__file__), 'triggers.sql')

#     with connection.cursor() as cursor:
#         # Check if the trigger already exists
#         cursor.execute("SHOW TRIGGERS LIKE 'after_user_delete';")
#         trigger_exists = cursor.fetchone()

#         if not trigger_exists:
#             with open(script_path, 'r') as f:
#                 cursor.execute(f.read())



#  *****************WORKING*********************

from django.db.backends.signals import connection_created
from django.dispatch import receiver
import os

# Add this global variable to track whether the trigger script has been executed
trigger_script_executed = False

@receiver(connection_created)
def activate_foreign_keys(sender, connection, **kwargs):
    global trigger_script_executed

    # Check if the trigger script has been executed before
    if not trigger_script_executed:
        script_path = os.path.join(os.path.dirname(__file__), 'triggers.sql')

        with connection.cursor() as cursor:
            # Check if the trigger already exists
            cursor.execute("SHOW TRIGGERS LIKE 'after_hostelite_delete';")
            trigger_exists = cursor.fetchone()

            if not trigger_exists:
                with open(script_path, 'r') as f:
                    cursor.execute(f.read())

        # Set the flag to True after executing the script
        trigger_script_executed = True

#  *****************WORKING*********************








# from django.db.backends.signals import connection_created
# from django.dispatch import receiver
# import os

# @receiver(connection_created)
# def activate_foreign_keys(sender, connection, **kwargs):
#     script_path = os.path.join(os.path.dirname(__file__), 'triggers.sql')

#     with connection.cursor() as cursor:
#         # Check if the trigger already exists
#         cursor.execute("SHOW TRIGGERS LIKE 'after_user_delete';")
#         trigger_exists = cursor.fetchone()

#         if not trigger_exists:
#             with open(script_path, 'r') as f:
#                 cursor.execute(f.read())
