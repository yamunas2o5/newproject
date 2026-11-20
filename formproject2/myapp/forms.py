
from django import forms
from myapp.models import Student

# class StudentForm(forms.Form):
#     name=forms.CharField()
#     age=forms.IntegerField()
#     place=forms.CharField()
#     email=forms.EmailField()
   
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'

    def clean_name(self):
        n=self.cleaned_data['name']
        if len(n)<3:
            raise forms.ValidationError("min no of character must greater than 3")
        return n

    def clean_age(self):
            a=self.cleaned_data['age']
            if a<=0:
                raise forms.ValidationError("age must be positive")
            return a