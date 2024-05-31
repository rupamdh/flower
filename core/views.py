from django.shortcuts import render
from shop.models import *

# Create your views here.
def home_page(request):
    cat_list = [2,3,4,5,6]
    categories = Category.objects.filter(id__in=cat_list)

    context = {
        'categories' : categories
    }
    return render(request, 'index.html', context)