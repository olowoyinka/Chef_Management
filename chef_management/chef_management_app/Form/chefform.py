from django import forms
from chef_management_app.models import Country



class AddChefForm(forms.Form):
    email=forms.EmailField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control"}))
    password=forms.CharField(label="Password",max_length=50,widget=forms.PasswordInput(attrs={"class":"form-control"}))
    first_name=forms.CharField(label="First Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(label="Last Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField(label="Username",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    chef_name=forms.CharField(label="Chef Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))


class EditChefForm(forms.Form):
    first_name=forms.CharField(label="First Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(label="Last Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    chef_name=forms.CharField(label="Chef Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))


class ChefPhoneForm(forms.Form):
    phone_number=forms.IntegerField(label="Phone Number",widget=forms.NumberInput(attrs={"class":"form-control"}))


class ChefAddressForm(forms.Form):
    name = forms.CharField(label="Address Location",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    countries = Country.objects.all()
    country_list = []
    for country in countries:
        small_couuntry = (country.id, country.name)
        country_list.append(small_couuntry)
    country = forms.ChoiceField(label="Country",choices=country_list,widget=forms.Select(attrs={"class":"form-control"}))


class EditChefAddressForm(forms.Form):
    name=forms.CharField(label="Address Location",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    countries=Country.objects.all()
    country_list = []
    for country in countries:
        small_couuntry = (country.id, country.name)
        country_list.append(small_couuntry)
    country = forms.ChoiceField(label="Country",choices=country_list,widget=forms.Select(attrs={"class":"form-control"}))