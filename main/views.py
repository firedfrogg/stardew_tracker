from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from main.models import Item
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.db.models import Min, Max


# Create your views here.
def show_main(request):
    items = Item.objects.all()
    item_count = sum(item.amount for item in items)
    item_total_worth = sum(item.calculate_total() for item in items)
    earliest_date = items.aggregate(earliest_date=Min('date_added'))['earliest_date'].day
    latest_date = items.aggregate(latest_date=Max('date_added'))['latest_date'].day

    context = {
        'application_name': 'Stardew Valley\'s Item Tracker',
        'name': 'Julian Alex',
        'class': 'PBP F',
        'items': items,
        'item_count': item_count,
        'item_total_worth': item_total_worth,
        'days_since_added': latest_date - earliest_date
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def delete_item(request, item_id):
    # Get the item object to delete
    item = get_object_or_404(Item, pk=item_id)

    if request.method == 'POST':
        # Delete the item if the request method is POST
        item.delete()
        return HttpResponseRedirect(reverse('main:show_main'))
    
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
