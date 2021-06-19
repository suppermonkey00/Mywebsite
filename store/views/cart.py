from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.product import Product
from django.http import HttpResponse
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator


class Cart(View):
    @method_decorator(auth_middleware)
    def get(self,request):
        ids= list(request.session.get('cart').keys())
        print('ids:',ids)
        products = Product.get_product_by_id(ids)
        print('product:',products)
        return render(request,'cart.html',{'products': products})

