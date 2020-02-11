from django import forms

from app.models import EpochModel


class EpochForm(forms.Form):
    epochtime = forms.DecimalField(required=True, decimal_places=0)
    # CHOICES = (
    # ('Sec', 'Seconds'), ('MilliSec', 'MilliSeconds'), ('MicroSec', 'MicroSeconds'), ('NanoSec', 'NanoSeconds'))
    # epochchoice = forms.CharField(label='Convert Into', widget=forms.Select(choices=CHOICES))
