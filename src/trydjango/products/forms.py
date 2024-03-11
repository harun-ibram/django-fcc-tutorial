from django import forms
from .models import Product

class ProductForm (forms.ModelForm):
    title       = forms.CharField(label='', 
                                  widget=forms.TextInput(attrs={
                                      "placeholder" : "Your Title Here"
                                      }
                                    )
                                )
    description = forms.CharField(
                            required=False, 
                            widget=forms.Textarea(
                                attrs= {
                                    "class" : "new-class-name",
                                    "id" : "new-id-here",
                                    "cols" : 120,
                                    "rows" : 20,

                                }
                            )
                            
                            )
    price       = forms.DecimalField(initial=1.99)
    email       = forms.EmailField()
    class Meta:
        model = Product
        fields= [
            'title',
            'description', 
            'price',
            'email'
        ]
    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get('title')
    #     if "uwu" not in title:
    #         raise forms.ValidationError("This is not a valid title")
    #     if "ara" not in title:
    #         raise forms.ValidationError("This is not a valid title")
    #     if "owo" not in title:
    #         raise forms.ValidationError("This is not a valid title")
    #     return title
    
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if "@" not in email:
            raise forms.ValidationError("This is not a valid email")
        if "." not in email:
            raise forms.ValidationError("This is not a valid email")
        return email


class RawProductForm (forms.Form):
    title       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder" : "Your Title Here"}))
    description = forms.CharField(
                            required=False, 
                            widget=forms.Textarea(
                                attrs= {
                                    "class" : "new-class-name",
                                    "id" : "new-id-here",
                                    "cols" : 120,
                                    "rows" : 20,

                                }
                            )
                            
                            )
    price       = forms.DecimalField(initial=1.99)