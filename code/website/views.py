from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.template import loader
from .models import inventory
from .forms import inventoryForm,serchForm

# Create your views here.

def home(request): 
    return render(request,'home.html',{})
    
def login_user(request):
    if(request.method=='POST'):
        username = request.POST['username']
        password = request.POST['password']

        # authenticate 
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"you have successfully logged in to the system!. ")
            return redirect('home')
        else:
            messages.success(request,"you are not logged in to the system !.Please login.")
            return redirect('login')
    else:
        return render(request,'login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out from the system!")
    return redirect('login')

def manage_store(request):        
    invForm = inventoryForm()
    if request.method == 'POST':
        invForm = inventoryForm(request.POST)
        print('invoice form : data : ',invForm.data)        
        if invForm.is_valid():            
            print('form is valid')            
            invForm.save()
            return redirect('store')
    template_name = 'store.html'
    context = {'form': invForm}
    return render(request, template_name, context)

def get_inventory(request):    
    inventory_obj = inventory.objects.all()
    list_inventory = []    
    print('get_inventory:inventory_obj:',inventory_obj)
    for i in inventory_obj:
        if (i.quantity_sold != None):
            available_qty = (i.quantity_avl - i.quantity_sold)
            dict_inventory = {
                "model_number": i.model_number,
                "model_name": i.model_name,
                "sold_quantity": i.quantity_sold,
                "actual_avb_quantity": available_qty
            }
            list_inventory.append(dict_inventory) 
            print("list inventory:",list_inventory)   
    template_name = 'inventory.html'    
    context = {'obj': inventory_obj , 'invList':list_inventory}
    return render(request, template_name, context)

def get_invoice(request): 
    total_sales_amount = 0   
    sold_obj = inventory.objects.values_list('model_number','model_name','make','unit_price','quantity_sold')
    print('get_invoice:sold_obj:',sold_obj)
    sale_items = []
    for i in sold_obj:
        if(i[4]!=None):
            print('sold quantity not None',i[4])
            sale_value = i[3]*i[4]
            print('sale value',sale_value) 
            total_sales_amount += sale_value
            sale_items.append({
                'model_number': i[0],
                'model_name': i[1],
                'make': i[2],
                'unit_price': i[3],
                'quantity_sold': i[4],
                'sale_value': sale_value
            })
    print('total_sales_value',total_sales_amount)       
    template_name = 'invoice.html' 
    context = {'sold_list': sale_items,'total':total_sales_amount}
    return render(request, template_name, context)

def search_bikes(request):
    srchForm = serchForm()
    search_obj = None
    if request.method == 'POST':
        srchForm = serchForm(request.POST)
        print('search form : data : ',srchForm.data)        
        if srchForm.is_valid():            
            print('form is valid')
            search_obj = inventory.objects.filter(model_name=srchForm.cleaned_data['model_name'],make=srchForm.cleaned_data['make'])              
            for s in search_obj:
                print('search obj : data : ',s.model_number ,s.model_name,s.make,s.yom,s.unit_price) 
    template_name = 'search.html'
    context = {'form': srchForm,'search_obj':search_obj}
    return render(request, template_name, context)