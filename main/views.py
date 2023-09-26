from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from main.models import Item
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.db.models import Min, Max
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime


@login_required(login_url='/login')
# Create your views here.
def show_main(request):
    items = Item.objects.filter(user=request.user)
    item_count = sum(item.amount for item in items)
    item_total_worth = sum(item.calculate_total() for item in items)
    earliest_date = Item.objects.filter(user=request.user).aggregate(earliest_date=Min('date_added'))['earliest_date']
    latest_date = Item.objects.filter(user=request.user).aggregate(latest_date=Max('date_added'))['latest_date']

    if earliest_date is not None and latest_date is not None:
        days_since_added = (latest_date - earliest_date).days
    else:
        days_since_added = 0;

    context = {
        'application_name': 'Stardew Valley\'s Item Tracker',
        'name': request.user.username,
        'class': 'PBP F',
        'items': items,
        'item_count': item_count,
        'item_total_worth': item_total_worth,
        'days_since_added': days_since_added + 1,
        'last_login': request.COOKIES['last_login']
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def delete_item(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    return redirect('main:show_main')

def reduce_amount(request, id):
    item = Item.objects.get(id=id)
    if item.amount > 0:
        item.amount -= 1
        item.save()
    return redirect('main:show_main')

def increase_amount(request, id):
    item = Item.objects.get(id=id)
    item.amount += 1
    item.save()
    return redirect('main:show_main')
    
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
    
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
