from django import forms

from company.models import Employee, Team


class EmployeeForm(forms.Form):
    
    name=forms.CharField(max_length=30)
    salary=forms.IntegerField()
    title=forms.CharField(max_length=30)
    # team=forms.ChoiceField(choices=[(team.pk,team.pk) for team in Team.objects.all()],required=False)
    team_name=forms.CharField(max_length=30)
    mana=forms.CharField(max_length=30)
    
    
    
class EmployeeForm2(forms.ModelForm):
    salary=forms.CharField(max_length=30)
    class Meta:
        model=Employee
        fields="__all__"
        exclude=['name']
    
