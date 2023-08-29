from django import forms

from catalog.models import Product, Version

FORBIDDEN_WORDS = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product

        fields = ('title', 'image', 'description', 'category', 'price', 'is_published')

    def clean_title(self):
        cleaned_data = self.cleaned_data['title']
        for word in FORBIDDEN_WORDS:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'Нельзя добавлять продукты с названием {word}')

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        for word in FORBIDDEN_WORDS:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'Нельзя добавлять продукты у которых в описании есть слово {word}')

        return cleaned_data


class ProductFormModerator(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('description', 'category', 'is_published')

    def clean_description(self):

        cleaned_data = self.cleaned_data['description']
        for word in FORBIDDEN_WORDS:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'Нельзя добавлять продукты у которых в описании есть слово {word}')

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        exclude = ('product',)
#        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
