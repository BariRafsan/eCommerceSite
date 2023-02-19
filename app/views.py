from django.shortcuts import render,redirect
from .forms import CreateUserForm, CustomerProfileForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.views import View
from django.db.models import Count
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Product,Cart,Order
from django.views.generic import ListView, DetailView

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
            
    context = {'form': form}
    return render(request, 'app/register.html', context)

def loginpage(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return render(request, 'app/login.html')
    
    return render(request, 'app/login.html', context)
def logutUser(request):
    logout(request)
    return redirect('login')

def homepage(request):
    return render(request, 'app/home.html')

class OrderView:
    order = Order



class CategoryView(View):
    def get(self,request,val):
        products = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')

        return render(request, 'app/category.html',locals())
class CategoryTitle(View):
    def get(self,request,val):
        products = Product.objects.filter(title=val)
        title = Product.objects.filter(category=products[0].category).values('title')
        return render(request, 'app/category.html',locals())
class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/product_detail.html',locals())

class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html',locals())
    def post(self,request):
        return render(request, 'app/profile.html',locals())
    

def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    if Cart.objects.filter(user=user,product=product).exists():
        cart = Cart.objects.get(user=user,product=product)
        cart.quantity += 1
        cart.save()
    else:  
        Cart(user = user,product=product).save()
    return redirect('/cart')
    

def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    size = len(cart)
    subtotal = 0.0
    whole = 0
    for item in cart:
        whole += item.quantity
        subtotal += (item.quantity * item.product.price)
    tax = subtotal * 0.1
    total = subtotal + tax
    print('size',size)
    return render(request, 'app/addtocart.html',locals())
def checkout(request):
    user = request.user
    cart_id = request.GET.get('cart_id')
    cart = Cart.objects.filter(user=user)
    
    for item in cart:
        Order(user=user,product=item.product,quantity=item.quantity,total_cost=item.total_cost).save()
        item.delete()
    return redirect('/')

def remove_from_cart(request):
    user = request.user
    cart_id = request.GET.get('cart_id')
    cart = Cart.objects.get(id=cart_id)
    if cart.quantity > 1:
        cart.quantity -= 1
        cart.save()
    else:
        cart.delete()
    return redirect('/cart')

def plus_to_cart(request):
    user = request.user
    cart_id = request.GET.get('cart_id')
    cart = Cart.objects.get(id=cart_id)
    cart.quantity += 1
    cart.save()
    return redirect('/cart')

# Inherit from OrderView
def order(request):

    user = request.user
    print(user)
    order = OrderView.order.objects.filter(user=user)
    #order = Order.objects.filter(user=request.user)
    tot=0
    for item in order:
        tot += item.total_cost
        
    return render(request, 'app/order.html',locals())


    


    