from django.shortcuts import render
from .models import Images

# Create your views here.
def index(request):
    all_data = Images.get_pixxies()


    return render(request, 'all_pixxies/index.html', {'all_data':all_data})

def single_photo(request, photo_id):
    try:
        photos = Images.objects.get(id = photo_id)
    except DoesNotExist:
        raise Http404()

    return render(request, 'all_pixxies/image.html', {'photos':photos})

