from django import forms
from .models import Pacote

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Pacote
        fields = ('id_do_pacote', 
                  'title', 
                  'version', 
                  'authors',
                  'owners',
                  'summary', 
                  'project_URL', 
                  'icon_URL', 
                  'description', 
                  'require_license_acceptance', 
                  'dependencia',
                  'installer_type',
                  'unattended_arguments',
                  )