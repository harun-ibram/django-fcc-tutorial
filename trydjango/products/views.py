from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        "my_form" : form
    }
    return render(request, "products/product_create.html", context)

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        "title" : obj.title,
        "description" : obj.description
    }
    return render(request, "products/product_detail.html", context)

def render_initial_data(request):
    initial_data = {
        'title': "default title",
        'description': "default description",
        'price' : 10.99
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
    context = {
        "my_form": form
    }
    return render(request, "products/product_create.html", context)

def dynamic_lookup_view(request, id):
    # obj = Product.objects.get(id=id)
    # obj = get_object_or_404(Product, id=id)
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        "object" : obj
    }
    return render(request, "products/product_detail.html", context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    # POST request      
    if request.method == "POST":
        # confirming delete
        obj.delete()
        return redirect('../../')
    context = {
        "object" : obj
    }
    return render(request, "products/product_delete.html", context)

def product_list_view(request):
    queryset = Product.objects.all()

    context = {
        "object_list":queryset
    }
    return render(request, "products/product_list.html", context)

# def product_create_view(request):
#     # print(request.GET)
#     # print(request.POST)
#     if request.method == "POST":
#         new_title = request.POST.get('title')
#         print(new_title)
#         # Product.products.create(title=new_title, ...)
#     context = {}
#     return render(request, "products/product_create.html", context)

# def product_create_view(request):
#     form = RawProductForm()
#     if request.method == "POST":
#         form = RawProductForm(request.POST)
#         if form.is_valid():
#             # data is good
#             print(form.cleaned_data )
#             Product.objects.create(**form.cleaned_data)
#         else: 
#             print(form.errors)
#     context = {
#         "my_form" : form,
#     }
#     return render(request, "products/product_create.html", context)