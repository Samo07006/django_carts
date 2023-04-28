from django.shortcuts import render
from .models import Product,Cart



def home(request):
    product_list = Product.objects.all()
    return render(request,'main/home.html',context={
        'product_list':product_list
    })

def cart(request):
    
    carts = Cart.objects.all()
    if request.method == 'POST':
        prod_id = request.POST.get('id')
        my_prod = Product.objects.get(id=prod_id)
        cart_list = Cart.objects.all().select_related('cart_prod').values_list('cart_prod__name',flat=True)

        if my_prod.name in cart_list:
            cart_prod = Cart.objects.get(cart_prod__name=my_prod.name)
            cart_prod.count +=1
            cart_prod.save()
        else:
            Cart.objects.create(cart_prod = my_prod)



    return render(request,'main/cart.html',context={
        'cart_list':carts
    })