from django.http  import Http404 
from django.shortcuts import render 
from gallery.models import Image, Location, Category


DoesNotExist = Http404()
# Create your views here.

def index(request):
    images =Image.objects.all()
    category = Category.objects.all()
    locations = Location.objects.all()
    return render(request, 'index.html' ,{"images":images , "category":category, "locations":locations} ) 

def mygallery(request):
    images =Image.objects.all()
    locations = Location.objects.all()
    return render(request, 'photo.html', {"images":images,  "locations":locations})

def mygallery_details(request, pk):
    image = Image.objects.get(pk=pk)
    context = {
        'image': image
    }
    return render(request, 'photo_details.html', context)

def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_categories = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search_results.html',{"message":message,"searched_categories": searched_categories})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search_results.html',{"message":message})

def location(request,pk):
    try:
        location = Location.objects.get(id =pk)
        images = Image.objects.filter(location=location)
    except DoesNotExist:
        raise Http404()
    return render(request, "search.html",{"location":location , "images":images })



