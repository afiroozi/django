from django import forms
from .models import Post


class PostForm(forms.ModelForm, forms.Form):
    day_time = forms.DateTimeField(
        label="Day Time",
        required=False,
    )
    class Meta:
        model = Post
        fields = [
            "title",
            "content"
        ]

    def __init__(self, *args, **kwargs):
        if kwargs.get('instance'):
            dayTime = kwargs['instance'].dayTime
            kwargs.setdefault('initial', {})['day_time'] = dayTime

        return super(PostForm, self).__init__(*args, **kwargs)


class contactForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    passwd = forms.CharField(required=True)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_base, provider = email.split("@")
        domain, extension = provider.split(".")
        if not extension == "com":
            raise forms.ValidationError("Please Correct Email 'COM' Extension!!")
        return email



