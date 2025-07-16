from django import forms

from core.models import Todo


class TodoCreateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['name', 'description', 'deadline']

        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date',
                                                }
                                        )
            }