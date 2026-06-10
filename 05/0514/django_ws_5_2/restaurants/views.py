from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurant
from .forms import RestaurantForm

# Create your views here.
def index(request): 
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants': restaurants
    }
    return render(request, 'restaurants/index.html', context)

def new(request):
    return render(request, 'restaurants/new.html')

def create(request):
    restaurant = Restaurant()
    restaurant.name = request.POST.get('name')
    restaurant.description = request.POST.get('description')
    restaurant.address = request.POST.get('address')
    restaurant.phone_number = request.POST.get('phone_number')
    restaurant.save()
    return redirect('restaurants:index')

def detail(request, restaurant_pk):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_pk)
    context = {
        'restaurant':restaurant,
    }
    return render(request, 'restaurants/detail.html', context)

def update(request, restaurant_pk):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_pk)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('restaurants:index')
        
    else:
        form = RestaurantForm(instance=restaurant)

    context = {
        'form': form,
        'restaurant': restaurant,
    }
    return render(request, 'restaurants/update.html', context)

def delete(request, restaurant_pk):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_pk)
    if request.method == 'POST':
        restaurant.delete()
        return redirect('restaurants:index')
    return redirect('restaurants:detail', restaurant.pk)