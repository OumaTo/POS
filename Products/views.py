from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.db.models import Q
from Products.forms import *
from Products.models import *
from django.contrib import messages

# Create your views here.
def Products(request):
    search = request.GET.get('search') if request.GET.get('search') != None else ''
        
    products = Product.objects.filter(
        Q(Name__icontains = search) | Q(Quantity__icontains = search) |
        Q(Brand__icontains = search) | Q(Expiry_Date__icontains = search) |
        Q(Distributor__icontains = search) | Q(Description__icontains = search) |
        Q(Manufactured_Date__icontains = search) | Q(Arrival_Date__icontains = search)

        )
    # else:
    #     products = Product.objects.filter()

    context = {
        'total':products.count(),
        'products':products
    }
    return render(request, 'Products/products.html', context)

def AddProducts(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = request.POST.get('Name')
            form.save()
            messages.success(request, f"records for {name} added Successfully")
            return redirect('/')
            
    context = {
        'form':form
    }
    return render(request, 'Products/add_products.html', context)

def DeleteProduct(request,pk):
    product = Product.objects.get(id=pk)

    context = {
        'product': product,
    }
        
    if request.method == 'POST':
        product.delete()
        messages.success(request, f' Records For {product.Name} Deleted Successfully')

        return redirect('/Products/')

    return render(request, 'Products/delete_product.html', context)


def UpdateProduct(request,pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES ,instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'{product.Name} Updated Successfully')
            return redirect('/Products/')

    return render(request, 'Products/update_product.html',{'form':form})


def distributor(request):
    pass

def category(request):
    form = CategoryForm()
    categories = Category.objects.all()
    
    context = {
        'form':form,
        'categories':categories,
    }

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        cat = request.POST.get('category')
        if form.is_valid():
            form.save()
            messages.success(request, f'Category {cat}  Added ')
    
    return render(request, 'Products/category.html', context)


def edit_category(request,pk):
    categories = Category.objects.all()
    categ = Category.objects.get(id=pk)
    
    context = {
        'form':CategoryForm(instance=categ),
        'categories':categories,
    }
    
    if request.method == "POST":
        form = CategoryForm(request.POST,instance=categ)
        cat = request.POST.get('category')
        if form.is_valid():
            form.save()
            messages.success(request, f'{cat} Category Updated')

            return redirect('/Products/Category/')
            
    return render(request, 'Products/category.html', context)

def delete_category(request,pk):
    Category.objects.get(id=pk).delete()
    return redirect('/Products/Category/')