from django.contrib.auth import get_user_model # Best way to get user model, other than models.py
from django.contrib import admin


from .models import RecipeIngredients, Recipe

User = get_user_model()

# TabularInline is horizontal, StackedInline vertical
# Comes with 3 fields
class RecipeIngredientsInline(admin.StackedInline):
    model = RecipeIngredients
    # fields = ['name', 'quantity', 'unit', 'directions']
    extra = 0
    readonly_fields = ['quantity_as_float', 'as_mks', 'as_imperial']

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientsInline]
    list_display = ['name', 'user']
    readonly_fields = ['timestamp', 'updated']
    raw_id_fields = ['user'] # You should always use this for users.

admin.site.register(Recipe, RecipeAdmin)
