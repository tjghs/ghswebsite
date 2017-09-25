import django.forms as forms
from .models import HourItem, HourRequest


class HourItemForm(forms.ModelForm):
    class Meta:
        model = HourItem
        fields = ['title', 'hours']


class HourRequestForm(forms.ModelForm):
    class Meta:
        model = HourRequest
        fields = ['date', 'count', 'description', 'item']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }

# date = models.DateField()
# user = models.ForeignKey(User, on_delete=models.CASCADE)
# count = models.IntegerField()
# description = models.CharField(max_length=50)
# item = models.ForeignKey('HourItem')
# approved = models.BooleanField(default=False)
