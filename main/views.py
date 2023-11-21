import json
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
from datetime import date
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotFound, JsonResponse
from django.views.decorators.http import require_http_methods
import datetime


@login_required(login_url='/login')
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
    today = date.today().day
    item = Item.objects.get(id=id)
    item.delete()
    return redirect('main:show_main')

def reduce_amount(request, id):
    today = date.today().day
    item = Item.objects.get(id=id)
    if item.amount > 1:
        item.amount -= 1
        item.save()
    else:
        delete_item(request, id)
    return redirect('main:show_main')

def increase_amount(request, id):
    today = date.today().day
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

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Item.objects.create(
            user = request.user,
            name = data["name"],
            price = int(data["price"]),
            description = data["description"],
            amount = int(data["amount"]),
            favorable_weather = data["favorable_weather"],
            season = data["season"],
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

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

def get_product_json(request):
    product_item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

def get_updated_data(request):
    user = request.user
    items = Item.objects.filter(user=user)
    
    item_count = sum(item.amount for item in items)
    item_total_worth = sum(item.calculate_total() for item in items)
    earliest_date = items.aggregate(earliest_date=Min('date_added'))['earliest_date']
    latest_date = items.aggregate(latest_date=Max('date_added'))['latest_date']

    if earliest_date and latest_date:
        days_since_added = (latest_date - earliest_date).days + 1
    else:
        days_since_added = 0

    return JsonResponse({
        'days_since_added': days_since_added,
        'item_count': item_count,
        'item_total_worth': item_total_worth
    })


@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        user = request.user
        amount = request.POST.get("amount");
        favorable_weather = request.POST.get("favorable_weather");
        season = request.POST.get("season");

        new_product = Item(name=name, price=price, description=description, user=user,
                           amount=amount, favorable_weather=favorable_weather, season=season)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def increase_amount_ajax(request):
    if request.method == 'POST':
        item_id = request.POST.get("id")
        try:
            item = Item.objects.get(id=item_id)
            item.amount += 1
            item.save()
            return JsonResponse({'status': 'success', 'message': 'Amount increased successfully', 'new_amount': item.amount})
        except Item.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Item not found'}, status=404)
    return HttpResponseNotFound()

@csrf_exempt
@require_http_methods(['DELETE'])
def delete_item_ajax(request, id):
    try:
        item = Item.objects.get(pk=id)
        item.delete()
        return JsonResponse({'status': 'success', 'message': 'Item deleted successfully'})
    except Item.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Item not found'}, status=404)
