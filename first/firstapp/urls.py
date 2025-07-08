from django.urls import path
from .views import base, admin_login, inserthostelite, display_hostelite_table, hostelite_detail, edit_hostelite, deletehostelite, insertfood, display_food_table, insertadmin, admin_detail, display_admin_table, deletefood, admin_detail_one, submit_feedback, get_feedback, submit_complaint, get_complaints

urlpatterns = [
    path('',base,name="base"),
    path('admin_login/', admin_login, name='admin_login'),
    path('inserthostelite/', inserthostelite, name="inserthostelite"),
    path('display_hostelite_table/', display_hostelite_table, name='display_hostelite_table'),
    path('hostelite_detail/<int:hid>/', hostelite_detail, name='hostelite_detail'),
    path('insertadmin/', insertadmin, name="insertadmin"),
    path('admin_detail/<int:aid>/', admin_detail, name='admin_detail'),
    path('admin_detail/<int:admin_id>/', admin_detail_one, name='admin_detail_one'),
    path('display_admin_table/', display_admin_table, name='display_admin_table'),
    path('edit_hostelite/<int:hid>/', edit_hostelite, name='edit_hostelite'), 
    path('deletehostelite/', deletehostelite, name="deletehostelite"), 
    path('insertfood/', insertfood, name='insertfood'),
    path('display_food_table/', display_food_table, name='display_food_table'),
    path('deletefood/', deletefood, name='deletefood    '),
    path('api/feedback/', submit_feedback, name='submit_feedback'),
    path('api/feedback/get/', get_feedback, name='get_feedback'),
    path('api/complaints/', submit_complaint, name='submit_complaint'),
    path('api/complaints/get/', get_complaints, name='get_complaints'),
]