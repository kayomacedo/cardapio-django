from django.contrib import admin
from .models import Sabor, Pizza, Ingrediente

class SaborAdmin(admin.ModelAdmin):
    list_display = ('nome',)

class PizzaAdmin(admin.ModelAdmin):
    list_display = ('sabor', 'preco', 'status')
    filter_horizontal = ('ingredientes',)

class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('nome',)

admin.site.register(Sabor, SaborAdmin)
admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Ingrediente, IngredienteAdmin)
