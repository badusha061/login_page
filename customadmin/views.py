from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect, render
from customadmin.models import CustomUser
from django.contrib.auth.models import User
from django.db.models import Q
# Create your views here.


def admin_panel(request):
    user = User.objects.all()
    if request.user.is_superuser:
        user = User.objects.all()


        query = request.GET.get('query')
        if query:
            user = user.filter(Q(username__icontains=query))

        context = {
            'user':user
        }
        return render(request, 'admin.html',context )
    else:
        return redirect("customadmin:adminlogin")


def add_views(request):
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
      

        user = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
           
        )
        user.save()
        return redirect('customadmin:admin_panel')

  
def edit_views(request):
    user = User.objects.all()
    context = {
        'user':user
    }

    return redirect(request, 'admin.html', context)


def update_views(request,id):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')

        user = User.objects.get(id=id) 
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email
        user.save()

        return redirect('customadmin:admin_panel')


def delete_views(request, id):
    user = User.objects.filter(id = int(id) )
    user.delete()
    return redirect('customadmin:admin_panel')


def adminlogin(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=user_name, password=password)
        if user and user.is_superuser:
            request.session['admin_name'] = user_name
            login(request, user)
            return redirect('customadmin:admin_panel')  
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
            return redirect('customadmin:adminlogin')  
    else:
        if request.user.is_superuser:
            return redirect("customadmin:admin_panel")
        
        return render(request, 'adminlogin.html')


def logout_view(request):
    logout(request)
    return redirect("customadmin:adminlogin") 
    