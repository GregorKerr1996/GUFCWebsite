from django import forms
from website.models import Report, News

class ReportForm(forms.ModelForm):

    news_cat = forms.ModelChoiceField(queryset = News.objects.all())
    title = forms.CharField(max_length = 128, widget =forms.TextInput(attrs = {"placeholder": "Report Title"}))
    text = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Enter text"} ))
    views = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
    date = forms.DateField(widget=forms.DateInput(format='%m/%d/%Y'))


    class Meta:
        model = Report
        fields = ("news_cat", "title","text","views","date")