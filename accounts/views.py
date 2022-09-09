
from django.shortcuts import render,redirect

from .decorator import allowed_users, unauthenticated_user
from .models import *
from .forms import *
from .filters import *
#defaul django form for authentication
# from django.contrib.auth.forms import UserCreationForm

#flash meesage for template
from django.contrib import messages

#authenticating user and login and logout
from django.contrib.auth import authenticate,login as auth_login,logout as django_logout

#restrict for user that didn't login
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='accounts:login')
#only admins are able to see home page
@allowed_users(allowed_roles=['admin'])
def home(request):
    context = {
        'customers' : Customer.objects.all(),
        'orders': Order.objects.all(),
        # 'total_orders': Order.objects.all().count(),
        'orders_delivered':Order.objects.filter(status='delivered').count(),
        'orders_pending':Order.objects.filter(status='pending').count(),
        'user':request.user
    }
    return render(request,'accounts/dashboard.html',context)



@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    context = {
        'products': Product.objects.all(),
    }
    return render(request,'accounts/products.html',context)



@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def customer(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    # first query all the orders 
    # second based on request data 
    filter = OrderFilter(request.GET,queryset = orders)
    # remake the var with the filtered data
    orders = filter.qs
    
    context = {
        'customer': customer,
        'orders':orders,
        'filter':filter
    }
    return render(request,'accounts/customer.html',context)



@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def createOrder(request):
    # The request method 'POST' indicates
    # that the form was submitted
    if request.method == 'POST':
        # print(request.POST)
        # Create a form instance with the submitted data
        form = OrderForm(request.POST)
        if form.is_valid():
             # If the form is valid, perform some kind of
            # operation, for example sending a message
            form.save()
            return redirect('/')
    form = OrderForm()
    context={
        'form':form
    }
    return render(request,'accounts/order_form.html',context)



@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def updateOrder(request,pk):
    #Prefilled the form
    order = Order.objects.get(id=pk)
    #Form with old data( Load up an instance)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        #Post with data(Declare a ModelForm with the instance)
        form = OrderForm(request.POST)
        #Validate data
        if form.is_valid():
            form.save()
            return redirect('/')
    context={
        'form':form,
    }
    return render(request,'accounts/order_form.html',context)

@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context={
        'order':order
    }
    return render(request,'accounts/delete_order.html',context)

def delete_customer(request,pk):
    customer = Customer.objects.get(id=pk)
    if request.method == 'POST' :
        customer.delete()
        return redirect('/')
    return render(request,'accounts/delete_customer.html',context={'customer':customer})

@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        # for i in form:
        #     print(i)
        if form.is_valid():
            #default group of registered users = customer
            user = form.save()
            #success message after registeration
            messages.success(request,"Account was created for '%s'."%user)
            #after registration send user to the login page
            return redirect('accounts:login')
            
    context = {
        'form':form,
    }
    return render(request,'accounts/register.html',context)


@unauthenticated_user
def login(request):
    if request.method=='POST':
        #grab username and password
        #name of the inputs in template
        username = request.POST.get('username')        
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        #if user is authenticated
        if user is not None:
            auth_login(request,user)
            return redirect('accounts:home')
        else:
            messages.info(request,'Username or password is incorrect')
    return render(request,'accounts/login.html',context={})

def logout(request):
    django_logout(request)
    return redirect('accounts:login')

@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    orders = request.user.customer.order_set.all()
    # print('Orders ',orders.filter(status='delivered'))
    context={
        'orders':orders,
        'orders_delivered':orders.filter(status='delivered').count(),
        'orders_pending':orders.filter(status='pending').count()
    }
    return render(request,'accounts/user.html',context)

@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
    u = request.user.customer
    form = CustomerForm(instance=u)

    if request.method == 'POST':
        form = CustomerForm(request.POST,request.FILES,instance=u)
        if form.is_valid:
            form.save()
            messages.info(request,'Your profile has updated successfully.')
    context={'form':form}
    return render(request,'accounts/account_settings.html',context)