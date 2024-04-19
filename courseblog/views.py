from django.shortcuts import render, redirect
from . models import *
from allauth.account.decorators import login_required
from .decorators import admin_only
from .forms import CoursesForm, ProductForm
from django.http import JsonResponse
import json



# Create your views here.
def homepage(request):
    list_courses = Courses.objects.all()
    context = {
        'courses': list_courses
    }
    return render(request, 'courseblog/index.html', context)

'''
def contactpage(request):
    return render(request, 'courseblog/contact.html')
'''

def coursespage(request):
    list_courses = Courses.objects.all()
    context = {
        'courses': list_courses
    }
    return render(request, 'courseblog/courses.html', context)


def course_details(request, course_slug):
    selected_course = Courses.objects.get(slug=course_slug)
    context = {
        'course': selected_course
    }
    return render(request, 'courseblog/courses_details.html', context)
'''
def aboutuspage(request):
    return render(request, 'courseblog/about_us.html')'''


def videocall(request):
    return render(request, "courseblog/videocall.html",)

@admin_only
def createCourse(request):
    form = CoursesForm()
    if request.method == 'POST':
        form = CoursesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }

    return render(request, "courseblog/course_form.html", context)

@admin_only
def updateCourse(request, course_slug):
    selected_course = Courses.objects.get(slug=course_slug)
    form = CoursesForm(instance=selected_course)
    if request.method == 'POST':
        form = CoursesForm(request.POST, instance=selected_course)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }

    return render(request, "courseblog/updatecourse_form.html", context)

@admin_only
def deleteCourse(request, course_slug):
    selected_course = Courses.objects.get(slug=course_slug)
    
    if request.method == 'POST':
        selected_course.delete()
        return redirect('/')   
    context = {
        'course': selected_course
    }

    return render(request, "courseblog/delete_course.html", context)

@admin_only
def createProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, "courseblog/product_form.html", context)

def updateProduct(request, product_uuid):
    selected_product = Product.objects.get(product_id=product_uuid)
    form = ProductForm(instance=selected_product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=selected_product)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }

    return render(request, "courseblog/updateproduct_form.html", context)


def deleteProduct(request, product_uuid):
    selected_product = Product.objects.get(product_id=product_uuid)
    
    if request.method == 'POST':
        selected_product.delete()
        return redirect('/')   
    context = {
        'product': selected_product
    }

    return render(request, "courseblog/delete_product.html", context)

'''
def shoppage(request):
    if request.user.is_authenticated:
        customer = request.user
        cart, created = Cart.objects.get_or_create(owner=customer, completed = False)
        cartitems = cart.cartitems_set.all()
    else:
        cart = []
        cartitems = []
        cart = {'cartquantity': 0}

    products = Product.objects.all()
    context = {'products': products, 'cart': cart, 'cartitems': cartitems}
    return render(request, 'courseblog/shop.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        cart, created = Cart.objects.get_or_create(owner=customer, completed = False)
        cartitems = cart.cartitems_set.all()
    else:
        cart = []
        cartitems = []
        cart = {'cartquantity': 0}
    context = {'cart': cart, 'cartitems': cartitems}
    return render(request, 'courseblog/cart.html', context)


def updateCart(request):
    data = json.loads(request.body)
    product_id = data['product_id']
    print(product_id)
    action = data['action']
    if request.user.is_authenticated:
        customer = request.user
        product = Product.objects.get(product_id=product_id)
        cart, created = Cart.objects.get_or_create(owner=customer, completed=False)
        cartitems, created = Cartitems.objects.get_or_create(product=product, cart=cart)

        if action == 'add':
            cartitems.quantity += 1
        cartitems.save()

        msg = {
            'quantity': cart.cartquantity
        }

    return JsonResponse(msg, safe=False)

def updateQuantity(request):
    data = json.loads(request.body)
    inputval = int(data['in_val'])
    product_id = data['p_id']
    if request.user.is_authenticated:
        customer = request.user
        product = Product.objects.get(product_id= product_id)
        cart, created = Cart.objects.get_or_create(owner=customer, completed=False)
        cartitems, created = Cartitems.objects.get_or_create(product=product, cart=cart)

        cartitems.quantity = inputval
        cartitems.save()

        msg = {
            'subtotal':cartitems.subtotal,
            'grandtotal': cart.grandtotal,
            'quantity': cart.cartquantity
        }

    return JsonResponse(msg, safe=False)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        cart, created = Cart.objects.get_or_create(owner=customer, completed = False)
        cartitems = cart.cartitems_set.all()
    else:
        cart = []
        cartitems = []
        cart = {'cartquantity': 0}
    context = {'cart': cart, 'cartitems': cartitems}
    return render(request, 'courseblog/checkout.html', context)

def payment(request):
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user
        total = float(data['cart_total'])
        cart, created = Cart.objects.get_or_create(owner=customer, completed=False)
        
        
        if total == cart.grandtotal:
            print(data['cart_total'])
            cart.completed = True
            cart.save()
        
        
        
    return JsonResponse('It is working', safe=False)
'''