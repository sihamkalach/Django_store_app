from django.shortcuts import render,redirect
from .models import Product
from .models import Category
from .models import Order, User
categories = Category.objects.all()
products = Product.objects.all()
def index(request) :
    new_products = [product for product in products if len(product.description) < 60]
    new_products = list(reversed(new_products))[:6]
    return render(request,'page_home.html',{'products': new_products , 'categories':categories})

def light (request): 
    lighting_category = Category.objects.get(name='Lighting')
    lighting_products = Product.objects.filter(category=lighting_category)
    return render(request,'Lighting.html',{'lighting_products':lighting_products,'categories':categories})

def furniture(request):
    furniture_category = Category.objects.get(name='Furniture')
    furniture_products = Product.objects.filter(category=furniture_category)
    return render(request,'Furniture.html',{'furniture_products':furniture_products,'categories':categories})

def sao(request):
    sao_category = Category.objects.get(name='Storage Organization')
    sao_products = Product.objects.filter(category=sao_category)
    return render(request,'Storage Organization.html',{'sao_products':sao_products,'categories':categories})

def art(request):
    wallart_category = Category.objects.get(name='Wall Art')
    wallart_products = Product.objects.filter(category=wallart_category)
    return render(request,'Wall Art.html',{'wallart_products':wallart_products,'categories':categories})

from django.shortcuts import render, redirect
from .models import User, Order

def buy(request, product_id):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        name = request.POST.get('name')
        telephone = request.POST.get('telephone')
        ville = request.POST.get('ville')
        address = request.POST.get('address')
        quantity = request.POST.get('quantity')
        
        # Vérifier si l'utilisateur existe déjà
        user, created = User.objects.get_or_create(
            name=name,
            telephone=telephone,
            ville=ville,
            address=address
        )
        
        # Récupérer le produit en fonction de son ID
        product = Product.objects.get(id=product_id)
        
        # Créer une instance Order et l'enregistrer dans la base de données
        order = Order.objects.create(product=product, user=user, quantity=quantity)
        
        # Rediriger l'utilisateur vers une page de confirmation ou toute autre page nécessaire
        return redirect('confirmation_page')  # Assurez-vous d'avoir une URL nommée pour la page de confirmation dans vos URLs
        
    else:
        # Si la méthode de requête n'est pas POST, afficher le formulaire
        return render(request, 'buy.html', {'product_id': product_id,'categories':categories})

def confirmation(request):
    return render(request, 'confirmation_page.html')
