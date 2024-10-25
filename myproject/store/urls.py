from django.urls import path
from . import views
urlpatterns =[
    path('',views.index,name='pagehome'),
    path('Lighting.html',views.light,name='lightpage'),
    path('Furniture.html',views.furniture,name='furniture'),
    path('Storage Organization.html',views.sao,name='SAOpage'),
    path('Wall Art.html',views.art,name='wallartpage'),
    path('buy/<int:product_id>/', views.buy, name='buy'),
    path('confirmation_page.html',views.confirmation,name='confirmation_page')
]