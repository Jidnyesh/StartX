from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm
from .models import Product,Job,Profile,Comments,Advertisement
from django.contrib.auth.models import User,Group

class SignUpForm(UserCreationForm):
    CATEGORY = (
        ('Start-up', 'Start-up'),
        ('Buyer', 'Buyer'),
        ('Advertiser', 'Advertiser'),
        ('User', 'User'),
    )
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Enter your username  Ex : Tom'}),label="")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': ' Enter your Password'}),label="")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': ' Enter your Confirm password'}),label="")
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Enter your first name  Ex : Tom'}),max_length=100,label="")
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Enter your last  Ex : cruze'}),max_length=100,label="")
    category = forms.ChoiceField(choices = CATEGORY ,label="")



    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
    class Meta:
        model = User
        fields = (
            'category',
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2',

        )

class AuthenticationLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Enter you UserName'}),label="")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': ' Enter your Password'}),label="")
    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )

class AddProductForm(forms.ModelForm):
    PRODUCT_CATEGORY = (
        ('Technology', 'Technology'),
        ('Sports', 'Sports'),
        ('Vehicles', 'Vehicles'),
        ('Audio', 'Audio'),
        ('Clothing','Clothing'),
        ('Furniture','Furniture'),
    )
    product_category = forms.ChoiceField(choices = PRODUCT_CATEGORY)
    class Meta:
        model = Product
        fields = ('title' , 'description' ,'price', 'patient_number' , 'image','product_category')

class AddJobForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.fields:
            self.fields[field].required = False
    class Meta:
        model = Job
        fields = (
            'job_title',
            'job_description',
            'required_skills',
            'requirements',
            'category',
            'income',
            'project_number',
            'location',
        )

class CompleteProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.fields:
            self.fields[field].required = False
    class Meta:
        model = Profile
        fields = (
            'company_name',
            'description',
            'image',

        )

class UserEditForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'password',
        )
        exclude = (
            'password',
            'password2'
        )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = (
            'text',
        )

class AddAdvertisementForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.fields:
            self.fields[field].required = False
    class Meta:
        model = Advertisement
        fields = (
            'title',
            'description',
            'category',
            'duration',
            'contact_number',
            'city',
            'location',
            'price',
        )
