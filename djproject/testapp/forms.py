from django import forms

class JobForm(forms.Form):
    company=forms.CharField(max_length=100);
    title=forms.CharField(max_length=100);
    eligibility=forms.CharField(max_length=100);
    address=forms.CharField(max_length=100);
    email=forms.EmailField();
    phonenumber=forms.IntegerField()
    date=forms.DateField();
