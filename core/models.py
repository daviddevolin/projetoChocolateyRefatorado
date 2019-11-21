from django.db import models

class Pacote (models.Model):
    #arquivonuspec
    id_do_pacote = models.CharField( max_length=50)
    title = models.CharField( max_length=50)
    version = models.IntegerField()
    authors = models.CharField( max_length=50)
    owners = models.CharField( max_length=50)
    summary = models.CharField( max_length=50)
    project_URL= models.CharField( max_length=50)
    icon_URL = models.URLField( max_length=200)
    description = models.TextField()
    require_license_acceptance = models.BooleanField()
    dependencia = models.CharField( max_length=50)
    #arquivo chocolatey install
    installer_type = models.CharField( max_length=3)
    unattended_arguments = models.CharField( max_length=50)
    URL = models.CharField( max_length=50)
    URL_64 = models.CharField( max_length=50)

    object = models.Manager()  
  
    
# Create your models here.
