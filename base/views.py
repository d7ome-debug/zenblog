from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base/index.html')

def about(request):
    return render(request, 'base/about.html')

def category(request):
    return render(request, 'base/category.html')

def search(request):
    return render(request, 'base/search-result.html')

def post(request, pk):
    return render(request, "base/single-post.html", {pk: pk})

def contact(request):
    return render(request, 'base/contact.html')
