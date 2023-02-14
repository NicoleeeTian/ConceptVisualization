from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from .models import MPTTModel


class GraphListForm(forms.Form):
    title = forms.CharField(max_length=200,required=True)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper = FormHelper
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            'title',
            Submit('submit','Submit',css_class='btn-success')
        )

class GraphForm(forms.Form):
    title = forms.CharField(max_length=200,required=True)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper = FormHelper
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            'title',
            Submit('submit','Submit',css_class='btn-success')
        )
