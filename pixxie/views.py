from django.shortcuts import render
from .models import Images,Category,Location

# Create your views here.
def index(request):
    all_data = Images.get_pixxies()

    photo_loc = Location.get_location()

    return render(request, 'all_pixxies/index.html', {'all_data':all_data, 'photo_loc':photo_loc})

def single_photo(request, photo_id):
    try:
        photos = Images.objects.get(id = photo_id)
    except DoesNotExist:
        raise Http404()

    return render(request, 'all_pixxies/image.html', {'photos':photos})


def search_results(request):
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')

        searched_categ = Category.search_category(search_term)
        message = f'{search_term}'

        searched_image = Images.get_pixxies_cat(searched_categ)

        return render(request, 'all_pixxies/search.html', {'message': message, 'photoz':searched_image})

    else:
        message = 'You havent searched for any item'
        return render(request, 'all_pxxies/search.html', {'message':message})


def location_pixxies(request,loct_id):

    pixxies_by_location = Images.pixxies_by_loct(loct_id)

    return render(request, 'all_pixxies/location.html', {'pixxies_by_location':pixxies_by_location})