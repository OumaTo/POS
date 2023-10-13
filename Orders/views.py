from xml.sax.handler import property_encoding
from django.http import HttpResponse
from django.shortcuts import redirect, render
from Products.models import Product
from Orders.forms import OrderForm
from Orders.models import Order
from django.contrib import messages

def status(orders):
    pending = []
    canceled = []
    completed = []

    for order in orders:
        if order.Status == 'Pending':
            vals = orders.count()
            pending.append(vals)

        elif order.Status == 'Canceled':
            vals = orders.count()
            canceled.append(vals)

        elif order.Status == 'Completed':
            vals = orders.count()
            completed.append(vals) 

    return canceled,pending,completed           



# Create your views here.
def Orders(request):

    search = request.GET.get('search') if request.GET.get('search') != None else ''

    orders = Order.objects.filter(Item__Name__icontains = search)

    
    # orders = Order.objects.all()
    canceled,pending,completed =status(orders)
     
    context ={
        'orders':orders,
        'Total': orders.count(),
        'pending': len(pending),
        'canceled': len(canceled),
        'completed': len(completed),
    }
    return render(request, 'Orders/orders.html',context)

def NewOrder(request):
    form = OrderForm()
    context ={
        'form':form,
    }
    if request.method == 'POST':

        form = OrderForm(request.POST)

        if form.is_valid():
            pro = form.cleaned_data['Item']
            q = form.cleaned_data['Quantity']
            
            product = Product.objects.filter(Name = pro).first()
            if product != None:
                Amount = product.Price
                price = int(Amount)* int(q)
                new_order = Order(Item=product, Quantity=q, Total=price, Status = 'Pending')

                new_order.save()
                messages.success(request,'Order Placed Successfully, Continue To checkout')
                return redirect('/Orders/Checkout/')

        
    return render(request, 'Orders/create_order.html',context)


def Checkout(request):
    latest = Order.objects.filter().last()
    context = {
        'products': latest,
    }
    return render(request, 'Orders/checkout.html', context)

def DeleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    context = {
        'order':order
    }

    if request.method == 'POST':
        order.delete()

        return redirect('/Orders/')
    
    return render(request, 'Orders/delete_order.html', context)


def Complete(request,pk):
    Order.objects.filter(id=pk).update(Status = 'Completed')
    
    return redirect('/Orders/')


def Cancel(request,pk):
    Order.objects.filter(id=pk).update(Status = 'Canceled')
    
    return redirect('/Orders/')