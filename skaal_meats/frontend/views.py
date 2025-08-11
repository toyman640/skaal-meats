from django.shortcuts import render

# Create your views here.
def index_view(request):
  return render(request, "index.html")



def about_us_view(request):
  return render(request, "about.html")


def contact_us_view(request):
  return render(request, "contact.html")


def shop_view(request):
  return render(request, "shop.html")




def more_info_view(request):
  content_id = request.GET.get("content", "1")  # Default to content 1 if missing
  return render(request, "more-info.html", {"content_id": content_id})


def error_404_view(request, exception=None):
  return render(request, "404.html", status=404)