from django import forms

# Register your forms here.

class FormCourse(forms.Form):
    name = forms.CharField(label='Nombre', max_length=100)
    name.widget.attrs['class'] = 'form-control'

