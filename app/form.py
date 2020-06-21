from django import forms
class Subscribe(forms.Form):
    Email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "email",                
                "class": "form-control"
            }
        )
    )
    
    subject = forms.CharField(
        widget=forms.Textarea(
            attrs={
                 "rows":"3",
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                 "rows":"3",
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    
    def __str__(self):
        return self.Email
    