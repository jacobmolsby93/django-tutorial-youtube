from django import forms 
from .models import Article


# a model form
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content'] # fields needs to include both fields in the model
    
    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        qs = Article.objects.all().filter(title__icontains=title) # filters down to an existing title
        if qs.exists():
            self.add_error("title", f"\"{title}\" is already in use. Please pick another title")
        return data

class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # def clean_title(self): # clean a specific field
    #     cleaned_data = self.cleaned_data # a dictionary
    #     print("cleaned_data", cleaned_data)
    #     title = cleaned_data.get('title')
    #     if title.lower().strip() == "the office":
    #         raise forms.ValidationError('this title is taken.')
    #     print("title", title)
    #     return title

    def clean(self): # clean all data
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title.lower().strip() == "the office":
            self.add_error('title', 'This title is taken')
            # raise forms.ValidationError('this title is taken.')
        if "office" in content or "office" in title.lower():
            self.add_error('content', "Office cannot be in content")
            raise forms.ValidationError("Office is not allowed")
        return cleaned_data

