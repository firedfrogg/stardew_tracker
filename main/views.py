from django.shortcuts import render


# Create your views here.
def show_main(request):
    context = {
        'application_name': 'Stardew Valley\'s Item Tracker',
        'name': 'Julian Alex',
        'item_name': 'Pufferfish',
        'season': 'Summ`er',
        'favorable_weather': 'Sun',
        'price': 200,
        'description': 'The Pufferfish is a fish that can be caught in the ocean at The Beach or on the Beach Farm on '
                       'sunny summer days between 12pm and 4pm, or on Ginger Island during any season on Island West '
                       '(ocean), South, Southeast, and in the Pirate Cove. It can also randomly be found in Garbage '
                       'Cans during Summer, or at the Traveling Cart for 600–1,000g.',
        'amount': 1
    }

    return render(request, "main.html", context)
