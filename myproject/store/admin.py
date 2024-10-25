from django.contrib import admin
from .models import Category , Product,User,Order
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Category,CategoryAdmin)

# 
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'display_category', 'description', 'image']

    def display_category(self, obj):
        return obj.category.name
    display_category.short_description = 'Category'
admin.site.register(Product,ProductAdmin)
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=['name','telephone','ville','address']
admin.site.register(User,UserAdmin)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['quantity','order_date','status']
admin.site.register(Order,OrderAdmin)