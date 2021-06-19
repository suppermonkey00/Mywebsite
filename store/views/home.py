from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.category import Category
from django.views import View
# Create your views here.


class Index(View):

    def get(self,request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart']= {}
        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products()
        data = {}
        data['products'] = products
        data['categories'] = categories
        print('you are:', request.session.get('email'))
        return render(request, 'index.html', data)

    def post(self,request):
        product = request.POST.get('product')
        print('product_id',product)
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        print('cart isexists',cart)
        if cart:
            quantity = cart.get(product)
            print('quantity',quantity)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity -1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print('cart', request.session['cart'])
        return redirect('homepage')









