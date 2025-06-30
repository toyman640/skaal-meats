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