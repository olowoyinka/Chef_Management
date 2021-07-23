from django import forms
from ckeditor.widgets import CKEditorWidget


class AddRecipeForm(forms.Form):
    name=forms.CharField(label="Name",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    description=forms.CharField(label="Description",widget=CKEditorWidget(attrs={"class":"form-control"}))
    method=forms.CharField(label="Method",widget=CKEditorWidget(attrs={"class":"form-control"}))
    ingredient=forms.CharField(label="Ingredient",widget=CKEditorWidget(attrs={"class":"form-control"}))
    price=forms.IntegerField(label="Price",widget=forms.NumberInput(attrs={"class":"form-control"}))

    image_url=forms.FileField(label="Main Image",max_length=50,widget=forms.FileInput(attrs={"class":"form-control"}))


class EditRecipeForm(forms.Form):
    name=forms.CharField(label="Name",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    description=forms.CharField(label="Description",widget=CKEditorWidget(attrs={"class":"form-control"}))
    method=forms.CharField(label="Method",widget=CKEditorWidget(attrs={"class":"form-control"}))
    ingredient=forms.CharField(label="Ingredient",widget=CKEditorWidget(attrs={"class":"form-control"}))
    price=forms.IntegerField(label="Price",widget=forms.NumberInput(attrs={"class":"form-control"}))

    image_url=forms.FileField(label="Main Image",max_length=50,widget=forms.FileInput(attrs={"class":"form-control"}), required=False)