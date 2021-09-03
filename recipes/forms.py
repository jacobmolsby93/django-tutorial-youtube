from django import forms


from .models import Recipe, RecipeIngredients

class RecipeForm(forms.ModelForm):
    error_css_class = 'error-field' # adds 'error-field' class to all elements in form
    required_css_class = 'required-field' # adds 'required-field' class to all elements in form
    name = forms.CharField(help_text='This is your help!')
    # description = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))
    # widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Recipe name"}), 
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'directions']
    
    # __init__ overwrites the statement in RecipeForm
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            print(field)    
            new_data = {
                "placeholder": f'Recipe {str(field)}',
                "class": 'form-control'
            }
            self.fields[str(field)].widget.attrs.update(
                new_data
            )  
        # # self.fields['name'].label = "" # Removes label already there
        # self.fields['name'].widget.attrs.update({'class': 'form-control-2'})
        self.fields['description'].widget.attrs.update({'rows': '2'})
        self.fields['directions'].widget.attrs.update({'rows': '4'})

class RecipeIngredientsForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredients
        fields = ['name', 'quantity', 'unit']
