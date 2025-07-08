from django.shortcuts import render,redirect, get_object_or_404
from .models import Hostelite, Food, Admin, Complaint
from django.db import connection

from .models import Feedback
from django.utils import timezone
from datetime import date
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
    
from django.http import JsonResponse

def base(request):  
    return render(request,'add_admin_form.html',{})


from django.contrib import messages

def admin_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        
        # Check 'admin' table
        try:
            admin = Admin.objects.get(email=email, password=password)
        except Admin.DoesNotExist:
            admin = None
        
        # Check 'hostelite' table if no match found in 'admin' table
        if admin is None:
            try:
                hostelite = Hostelite.objects.get(email=email, password=password)
            except Hostelite.DoesNotExist:
                hostelite = None
        
        # Authenticate user
        if admin:
            request.session['admin_id'] = admin.aid
            return JsonResponse({'success': True, 'user_type': 'admin', 'user_id': admin.aid})
        elif hostelite:
            request.session['hostelite_id'] = hostelite.hid
            return JsonResponse({'success': True, 'user_type': 'hostelite', 'user_id': hostelite.hid})
        else:
            return JsonResponse({'success': False, 'message': 'Incorrect email or password.'})
    else:
        return JsonResponse({'success': False, 'message': 'Method not allowed.'}, status=405)


    

def admin_detail(request):

    admin_id = request.session.get('admin_id')

    

    if admin_id:

        sql = """

            SELECT admin.aid, admin.name, admin.email, admin.contact_no,

                   admin.gender, admin.address, admin.password

            FROM admin

            WHERE admin.aid = %s

        """

        with connection.cursor() as cursor:

            cursor.execute(sql, [admin_id])

            columns = [col[0] for col in cursor.description]

            admin_data = cursor.fetchone()



        if admin_data:

            admin = dict(zip(columns, admin_data))

            return JsonResponse({'admin': admin})  # Returning the logged-in admin object



    return JsonResponse({'error': 'Admin not found'}, status=404)


def admin_detail_one(request, admin_id):
    if admin_id:
        sql = """
            SELECT admin.aid, admin.name, admin.email, admin.contact_no,
                   admin.gender, admin.address, admin.password
            FROM admin
            WHERE admin.aid = %s
        """
        with connection.cursor() as cursor:
            cursor.execute(sql, [admin_id])
            columns = [col[0] for col in cursor.description]
            admin_data = cursor.fetchone()

        if admin_data:
            admin = dict(zip(columns, admin_data))
            return JsonResponse({'admin': admin})

    return JsonResponse({'error': 'Admin not found'}, status=404)

def insertadmin(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact_no = request.POST.get('contact_no')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        password = request.POST.get('password')

        sql = """
            INSERT INTO admin (
                name, email, contact_no, gender, address, password
            ) VALUES (%s, %s, %s, %s, %s, %s)
        """
        params = [
            name, email, contact_no, gender, address, password
        ]

        with connection.cursor() as cursor:
            cursor.execute(sql, params)

        connection.commit()

        # Construct JSON response
        response_data = {'success': True, 'message': 'Admin inserted successfully'}
        return JsonResponse(response_data)

    # Return error response if request method is not POST
    response_data = {'success': False, 'message': 'Method not allowed'}
    return JsonResponse(response_data, status=405)



import json

from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

from django.db import connection


def inserthostelite(request):
    if request.method == "POST":
        # Parse JSON body of request
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        contact_no = data.get('contact_no')
        gender = data.get('gender')
        room_no = data.get('room_no')
        room_type = data.get('room_type', 'NON AC')  # Default value if not provided
        date_of_joining = data.get('date_of_joining')
        course_detail = data.get('course_detail')
        father_name = data.get('father_name')
        mother_name = data.get('mother_name')
        father_contact_no = data.get('father_contact_no')
        mother_contact_no = data.get('mother_contact_no')
        address = data.get('address')

        sql = """
            INSERT INTO hostelite (
                name, email, password, contact_no, gender, room_no, room_type, date_of_joining,
                course_detail, father_name, mother_name, father_contact_no, mother_contact_no, address
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = [
            name, email, password, contact_no, gender, room_no, room_type, date_of_joining,
            course_detail, father_name, mother_name, father_contact_no, mother_contact_no, address
        ]

        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            connection.commit()  # Commit the transaction

        # Construct JSON response
        response_data = {'success': True, 'message': 'Hostelite inserted successfully'}
        return JsonResponse(response_data)

    # Return error response if request method is not POST
    response_data = {'success': False, 'message': 'Method not allowed'}
    return JsonResponse(response_data, status=405)




@csrf_exempt

def insertfood(request):

    if request.method == "POST":

        data = json.loads(request.body)  # Parse the JSON data from the request body

        date = data.get('date')

        breakfast = data.get('breakfast')

        lunch = data.get('lunch')

        dinner = data.get('dinner')



        sql = """

            INSERT INTO food (date, breakfast, lunch, dinner)

            VALUES (%s, %s, %s, %s)

        """

        params = [date, breakfast, lunch, dinner]



        with connection.cursor() as cursor:

            cursor.execute(sql, params)



        # connection.commit()



        return JsonResponse({'success': True, 'message': 'Food entry added successfully'})



    return JsonResponse({'success': False, 'message': 'Method not allowed'}, status=405)


    
def display_admin_table(request):
    search_aid = request.GET.get('search_aid')

    if search_aid:
        sql = "SELECT aid, name, contact_no, email FROM admin WHERE aid = %s"
        params = [search_aid]

        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            admins = dictfetchall(cursor)
    else:
        admins = Admin.objects.values('aid', 'name', 'contact_no', 'email')

    # return render(request, 'display_admin_table.html', {'admins': admins})
    return JsonResponse({'admins': list(admins)})

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]







def display_hostelite_table(request):
    search_hid = request.GET.get('search_hid')

    if search_hid:
        sql = "SELECT hid, name, contact_no, email, room_no, room_type FROM hostelite WHERE hid = %s"
        params = [search_hid]

        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            hostelites = dictfetchall(cursor)
    else:
        hostelites = Hostelite.objects.values('hid', 'name', 'contact_no', 'email', 'room_no', 'room_type')

    return JsonResponse({'hostelites': list(hostelites)})

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]




def display_food_table(request):
    search_fid = request.GET.get('search_fid')

    if search_fid:
        sql = "SELECT fid, date, breakfast, lunch, dinner FROM food WHERE fid = %s"
        params = [search_fid]

        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            foods = dictfetchall(cursor)
    else:
        foods = Food.objects.values('fid', 'date', 'breakfast', 'lunch', 'dinner')

    return JsonResponse({'foods': list(foods)})

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def hostelite_detail(request, hid):
    try:
        hostelite = Hostelite.objects.get(hid=hid)
        hostelite_data = {
            'hid': hostelite.hid,
            'name': hostelite.name,
            'email': hostelite.email,
            'contact_no': hostelite.contact_no,
            'gender': hostelite.gender,
            'room_no': hostelite.room_no,
            'room_type': hostelite.room_type,
            'date_of_joining': hostelite.date_of_joining.strftime('%Y-%m-%d'),
            'course_detail': hostelite.course_detail,
            'father_name': hostelite.father_name,
            'mother_name': hostelite.mother_name,
            'father_contact_no': hostelite.father_contact_no,
            'mother_contact_no': hostelite.mother_contact_no,
            'address': hostelite.address
        }
        return JsonResponse({'hostelite': hostelite_data})
    except Hostelite.DoesNotExist:
        return JsonResponse({'error': 'Hostelite not found'}, status=404)





def deletefood(request):
    if request.method == "POST":
        data = json.loads(request.body)
        fid = data.get('fid')

        try:
            # Assuming Food model has a primary key 'fid'
            food = Food.objects.get(fid=fid)
            food.delete()
            return JsonResponse({'success': True})
        except Food.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Food entry not found'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)

    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)
    
def admin_detail(request):

    admin_id = request.session.get('admin_id')

    

    if admin_id:

        sql = """

            SELECT admin.aid, admin.name, admin.email, admin.contact_no,

                   admin.gender, admin.address, admin.password

            FROM admin

            WHERE admin.aid = %s

        """

        with connection.cursor() as cursor:

            cursor.execute(sql, [admin_id])

            columns = [col[0] for col in cursor.description]

            admin_data = cursor.fetchone()



        if admin_data:

            admin = dict(zip(columns, admin_data))

            return JsonResponse({'admin': admin})  # Returning the logged-in admin object



    return JsonResponse({'error': 'Admin not found'}, status=404)

@csrf_exempt
def edit_hostelite(request, hid):
    hostelite = get_object_or_404(Hostelite, hid=hid)

    if request.method == "PUT":
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        contact_no = data.get('contact_no')
        gender = data.get('gender')
        room_no = data.get('room_no')
        room_type = data.get('room_type', 'NON A/C')
        date_of_joining = data.get('date_of_joining')
        course_detail = data.get('course_detail')
        father_name = data.get('father_name')
        mother_name = data.get('mother_name')
        father_contact_no = data.get('father_contact_no')
        mother_contact_no = data.get('mother_contact_no')
        address = data.get('address')

        hostelite.name = name
        hostelite.email = email
        hostelite.contact_no = contact_no
        hostelite.gender = gender
        hostelite.room_no = room_no
        hostelite.room_type = room_type
        hostelite.date_of_joining = date_of_joining
        hostelite.course_detail = course_detail
        hostelite.father_name = father_name
        hostelite.mother_name = mother_name
        hostelite.father_contact_no = father_contact_no
        hostelite.mother_contact_no = mother_contact_no
        hostelite.address = address

        hostelite.save()

        return JsonResponse({'message': 'Hostelite updated successfully'})
    elif request.method == "GET":
        hostelite_data = {
            'hid': hostelite.hid,
            'name': hostelite.name,
            'email': hostelite.email,
            'contact_no': hostelite.contact_no,
            'gender': hostelite.gender,
            'room_no': hostelite.room_no,
            'room_type': hostelite.room_type,
            'date_of_joining': hostelite.date_of_joining,
            'course_detail': hostelite.course_detail,
            'father_name': hostelite.father_name,
            'mother_name': hostelite.mother_name,
            'father_contact_no': hostelite.father_contact_no,
            'mother_contact_no': hostelite.mother_contact_no,
            'address': hostelite.address
        }
        return JsonResponse(hostelite_data)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


def deletehostelite(request):
    if request.method == "POST":
        data = json.loads(request.body)
        hid = data.get('hid')

        sql = "DELETE FROM hostelite WHERE hid = %s"
        params = [hid]

        with connection.cursor() as cursor:
            cursor.execute(sql, params)
        
        connection.commit()

        # Return a JSON response indicating success
        return JsonResponse({'success': True})

    # Return a JSON response for other HTTP methods or invalid requests
    return JsonResponse({'success': False, 'message': 'Invalid request'}, status=405)




def edit_admin(request, aid):
    admin = get_object_or_404(Admin, aid=aid)

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact_no = request.POST.get('contact_no')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        password = request.POST.get('password')

        sql = """
            UPDATE admin SET
                name = %s, email = %s, contact_no = %s, gender = %s, address = %s, password = %s
            WHERE aid = %s
        """
        params = [
            name, email, contact_no, gender, address, password, aid
        ]

        with connection.cursor() as cursor:
            cursor.execute(sql, params)

        connection.commit()

        return redirect('admin_detail', aid=admin.aid)
    else:
        return render(request, 'edit_admin.html', {'admin': admin})



def deleteadmin(request):
    if request.method == "POST":
        aid = request.POST.get('aid')

        sql = "DELETE FROM admin WHERE aid = %s"
        params = [aid]

        with connection.cursor() as cursor:
            cursor.execute(sql, params)
        
        connection.commit()

    return render(request, "add_admin_form.html", {})


@csrf_exempt
def submit_feedback(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print("Received data:", data)  # Log received data

        hid = data.get('hid')
        print("hid value:", hid)  # Log value of hid

        if not hid:
            return JsonResponse({'error': 'Hostelite ID (hid) is required'}, status=400)

        date_str = data.get('date')
        if date_str:
            try:
                date = timezone.datetime.strptime(date_str, '%Y-%m-%d').date()
            except ValueError:
                return JsonResponse({'error': 'Invalid date format'}, status=400)
        else:
            date = timezone.now().date()

        room_no = data.get('room_no')
        ques1 = data.get('ques1', '')
        ques2 = data.get('ques2', '')
        ques3 = data.get('ques3', '')
        ques4 = data.get('ques4', '')

        rating = data.get('rating')
        if rating is not None:
            try:
                rating = int(rating)
            except ValueError:
                return JsonResponse({'error': 'Invalid rating value'}, status=400)
        else:
            rating = 0

        suggestions = data.get('suggestions', '')

        feedback = Feedback(
            hid=hid,
            date=date,
            room_no=room_no,
            ques1=ques1,
            ques2=ques2,
            ques3=ques3,
            ques4=ques4,
            rating=rating,
            suggestions=suggestions
        )
        feedback.save()

        return JsonResponse({'message': 'Feedback submitted successfully'})

    return JsonResponse({'error': 'Invalid request method'}, status=400)



@csrf_exempt
def get_feedback(request):
    if request.method == 'GET':
        feedbacks = Feedback.objects.all().values()
        feedback_list = list(feedbacks)
        return JsonResponse(feedback_list, safe=False)

    return JsonResponse({'error': 'Invalid request method'}, status=400)



@csrf_exempt
def submit_complaint(request):
    if request.method == 'POST':
        # data = request.POST
        data = json.loads(request.body)

        print("Received data:", data)  # Log received data

        hid = data.get('hid')
        print("hid value:", hid)  # Log value of hid

        if not hid:
            return JsonResponse({'error': 'Hostelite ID (hid) is required'}, status=400)

        date_str = data.get('date')
        if date_str:
            date = date_str
        else:
            return JsonResponse({'error': 'Date is required'}, status=400)

        room_no = data.get('room_no')
        complaint_type = data.get('complaint_type')
        description = data.get('description')

        complaint = Complaint(
            hid=hid,
            date=date,
            room_no=room_no,
            complaint_type=complaint_type,
            description=description
        )
        complaint.save()

        return JsonResponse({'message': 'Complaint submitted successfully'})

    return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def get_complaints(request):
    if request.method == 'GET':
        complaints = Complaint.objects.all().values()
        complaint_list = list(complaints)
        return JsonResponse(complaint_list, safe=False)

    return JsonResponse({'error': 'Invalid request method'}, status=400)
