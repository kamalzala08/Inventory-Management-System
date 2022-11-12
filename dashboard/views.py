from django.shortcuts import render , redirect
from django.http import HttpRequest,HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product,Order
from .forms import ProductForm  , OrderForm

from django.contrib.auth.models import User
# Create your views here.

@login_required
def index(request): 
    orders = Order.objects.all()
    products = Product.objects.all()
    
        
    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.orderby = request.user
            
            for i in products:
                
                if(i.name == str(instance.product)):
                    if(i.quantity >= int(instance.order_quantity)):
                        print("Orderd ..!")
                        instance.save()
                    else:
                        return render(request, 'dashboard/index.html',{'error':'quantity ..!'})
                    
                    
            return redirect('dashboard-index')
    else:
        form = OrderForm()
        
    context = {
        'orders':orders,
        'form':form,
        'products':products
    }
    return render(request, 'dashboard/index.html',context)

@login_required
def staff(request): 
    workers = User.objects.all()
    
    context = {
        'workers':workers,
    }
    return render(request, 'dashboard/staff.html',context)

@login_required
def products(request): 
    items = Product.objects.all()
    # items = Product.objects.raw("select * from dashboard_product")
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-products')
    else:
        form = ProductForm()

    context = { 
        'items':items,
        'form':form
    }
    
    
    return render(request, 'dashboard/product.html',context)

@login_required
def orders(request): 
    orders = Order.objects.all()
    i = [i for i in range(1,len(orders)+1)]
    context = {
        'orders':orders,
         'i':i
    }
    return render(request, 'dashboard/order.html',context)

@login_required
def product_delete(request,pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-products')
    context = {
        'item': item
    }
    return render(request, 'dashboard/product_delete.html', context)

@login_required
def product_update(request,pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-products')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/product_update.html', context)

@login_required
def staff_detail(request,pk):
    user = User.objects.get(id=pk)
    context = {
        'user':user
    }
    return render(request, 'dashboard/staff_details.html',context)
