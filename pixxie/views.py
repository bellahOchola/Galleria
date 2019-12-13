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


def search_results(request):
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        searched_images = Images.search_by_category(search_term)
        message = f'{search_term}'

        return render(request, 'all_pixxies/search.html', {'message': message, 'photoz':searched_images})

    else:
        message = 'You havent searched for any item'
        return render(request, 'all_pxxies/search.html', {'message':message})
