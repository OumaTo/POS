from django.http import HttpResponse, FileResponse
from django.shortcuts import redirect, render
from datetime import datetime
from reportlab.pdfgen import canvas
from Products.models import *
from io import BytesIO
from reportlab.pdfgen import canvas
from Products.forms import *
from django.contrib import messages

# Create your views here.


def generate_pdf_file():
    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    books = Product.objects.all()
    p.drawString(100, 750, "Book Catalog")
    # p.drawInlineImage('nmp.jpg', 100, 730)

    y = 700
    for book in books:
        p.drawString(100, y, f"Title: {book.Name}")
        p.drawString(100, y - 20, f"Author: {book.Quantity}")
        p.drawString(100, y - 40, f"Year: {book.Manufactured_Date}")
        y -= 60

    p.showPage()
    p.save()
    
    buffer.seek(0)
    return buffer
    

def index(request):
    time = datetime.now()
    context = {
        'time': time,
        'hour': time.hour,
        'products_total': Product.objects.all().count(),
    }

    
    return render(request, 'PosApp/index.html', context)



def home(request):
    response = FileResponse(generate_pdf_file(), as_attachment=True, filename='book_catalog.pdf')

    return response


def shelf(request):
    shelves = Shelf.objects.all()
    form = ShelfForm()
        
    context = {
        'form':form,
        'shelves':shelves,
    }

    if request.method == "POST":
        form = ShelfForm(request.POST)
        shelf = request.POST.get('shelf_no')
        if form.is_valid():
            form.save()
            messages.success(request, f'Shelf {shelf} Added Successfully')
            
    return render(request, 'PosApp/shelves.html', context)


def edit_shelf(request,pk):
    shelf = Shelf.objects.get(id=pk)
    form = ShelfForm(instance=shelf)
    shelves = Shelf.objects.all()
        
    context = {
        'form':form,
        'shelves':shelves,
    }
    
    if request.method == "POST":
        form = ShelfForm(request.POST, instance=shelf)
        shelf = request.POST.get('shelf_no')
        if form.is_valid():
            form.save()
            messages.success(request, f'Shelf {shelf} Updated')

            return redirect('/shelf/')
            
    return render(request, 'PosApp/shelves.html', context)

def delete_shelf(request,pk):
    Shelf.objects.get(id=pk).delete()
    return redirect('/shelf/')
