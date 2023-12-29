from django import forms

from Fruitipedia.fruits.models import Fruit
from Fruitipedia.profiles.models import Profile


class CreateProfileFrom(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }

        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'


class DeleteFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = "__all__"
        # exclude = ('owner',)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields.values():
    #         field.widget.attrs['disabled'] = True
