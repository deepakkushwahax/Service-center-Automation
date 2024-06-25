from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def home(request):
    key = request.session.get('session_key')
    feedback = Feedback.objects.all()
    user = None
    if key:
        try:
            user = User.objects.get(phone=key)
            return render(request, 'html/home.html', {'user':user, 'feedback':feedback})
        except:
            user = AdminMod.objects.get(aid=key)
            return render(request, 'html/home.html', {'user':user,'feedback':feedback})
    else:
        return render(request, 'html/home.html', {'feedback':feedback})


def register(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        password = request.POST['password']
        name = request.POST['name']
        email = request.POST['email']
        pic = request.FILES.get('pic')
        address = request.POST['address']
        
        x = User.objects.filter(phone=phone)
        y = User.objects.filter(email=email)
        
        if x or y:
            messages.error(request, 'Same Number or Email Exist!!!')
            return render(request, 'user/register.html')
            
        obj = User()
        obj.phone=phone
        obj.password=password
        obj.name=name
        obj.email=email
        obj.pic=pic
        obj.address=address
        obj.save()
        messages.success(request, 'Registered Successfully')
        return redirect('login')
    else:
        return render(request, 'user/register.html')



def login(request):
    if request.method =='POST':
        phone = request.POST['phone']
        password = request.POST['password']
        obj = User.objects.filter(phone=phone, password=password)
        if len(obj)>0:
            request.session['session_key'] = phone
            return redirect('home')
        else:
            messages.error(request, 'Wrong Credentials')
            return redirect('login')
    else:
        return render(request, 'user/login.html')
    



def booking(request, phone):
    key = request.session.get('session_key')
    if key:
        user = User.objects.get(phone=key)
        company = Company.objects.get(phone=phone)
        if request.method == 'POST':
            vehicle = request.FILES.get('vpic')
            vcom = request.POST['vcom']
            vname = request.POST['vname']
            vnum = request.POST['vnum']
            obj = Booking()
            obj.user = user
            obj.company = company
            obj.vehicle_img = vehicle
            obj.vehicle_number = vnum
            obj.vehicle_name = vname
            obj.vehicle_company = vcom
            obj.save()
            messages.success(request, 'Booking Successfull')
            return redirect('bookings')
        else:
            key = request.session.get('session_key')
            user = User.objects.get(phone=key)
            company = Company.objects.get(phone=phone)
            return render(request, 'user/booking.html', {'user':user, 'company':company})
    else:
        return redirect('login')



def bookings(request):
    key = request.session.get('session_key')
    user = User.objects.get(phone=key)
    bookings = Booking.objects.filter(user=user)
    return render(request, 'user/bookings.html', {'bookings':bookings, 'user':user})


def companies(request):
    key = request.session.get('session_key')
    user = None
    if key:
        user = User.objects.get(phone=key)
    company = Company.objects.filter(status=True)
    return render(request, 'html/companies.html', {'companies':company, 'user':user})


def bookcompanies(request,type_of_vehicle ):
    key = request.session.get('session_key')
    user = None
    if key:
        user = User.objects.get(phone=key)
    company = Company.objects.filter(type_of_vehicle=type_of_vehicle, status=True)
    return render(request, 'html/bookcompanies.html', {'company':company, 'user':user})


def feedback(request, id):
    b_id = Booking.objects.get(id=id)
    if request.method == "POST": 
        rating = request.POST['rating']
        remark = request.POST['remark']
        obj = Feedback()
        obj.booking = b_id
        obj.rating = rating
        obj.remark = remark
        obj.save()
        messages.success(request, 'Feedback Submitted')
        return redirect('bookings')
    else:
        key = request.session.get('session_key')
        user = User.objects.get(phone=key)
        return render(request, 'user/feedback.html', {'user':user})

def pcom(request):
    company = Company.objects.filter(status=False)
    return render(request, 'html/pendingcompanies.html', {'companies':company})


def feedbacks(request):
    obj = Feedback.objects.all()
    return render(request, 'html/feedbacks.html', {'feedback':obj})


def approve(request, id):
    obj = Company.objects.get(id=id)
    obj.status = True
    obj.save()
    messages.success(request, 'Approved')
    return redirect('adminhome')


def reject(request, id):
    obj = Company.objects.get(id=id)
    obj.delete()
    messages.success(request, 'Rejected')
    return redirect('adminhome')



def adminlog(request):
    if request.method =='POST':
        id = request.POST['id']
        password = request.POST['password']
        obj = AdminMod.objects.filter(aid=id, password=password)
        if len(obj)>0:
            request.session['session_key'] = id
            return redirect('adminhome')
        else:
            messages.error(request, 'Wrong Credentials')
            return redirect('adminlog')
    else:
        return render(request, 'html/adlogin.html')
    

def adminhome(request):
    key = request.session.get('session_key')
    if key:
        obj = AdminMod.objects.get(aid=key)
        book_obj = Booking.objects.all()
        return render(request, 'html/adminhome.html', {'user':obj, 'bookings':book_obj})
    else:
        return redirect('adminlog')


def forgetpassword(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        password = request.POST['password']
        name = request.POST['name']
        email = request.POST['email']
        try:
            x = User.objects.get(phone=phone, name=name, email=email)
            x.phone=phone
            x.password=password
            x.name=name
            x.email=email
            x.save()
            messages.success(request, 'Password Changed Successfully')
            return redirect('login')
        except:
            messages.error(request, 'Details Not Found')
            return render(request, 'user/forgetpassword.html')
    else:
        return render(request, 'user/forgetpassword.html')



def compregister(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        name = request.POST['name']
        email = request.POST['email']
        pic = request.FILES.get('pic')
        idcard = request.FILES.get('idcard')
        address = request.POST['address']
        typeof = request.POST['type']
        desc = request.POST['desc']
        
        x = Company.objects.filter(phone=phone)
        y = Company.objects.filter(email=email)
        
        if x or y:
            messages.error(request, 'Same Number or Email Exist!!!')
            return render(request, 'html/compreg.html')
            
            
        obj = Company()
        obj.phone=phone
        obj.name=name
        obj.email=email
        obj.pic=pic
        obj.idcard=idcard
        obj.type_of_vehicle=typeof
        obj.description=desc
        obj.location=address
        obj.save()
        messages.success(request, 'Company Registered Successfully')
        return redirect('home')
    else:
        return render(request, 'html/compreg.html')



def logout(request):
    request.session.flush()
    return redirect('home')