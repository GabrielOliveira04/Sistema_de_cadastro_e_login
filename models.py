from django.db import models


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    firstname = models.TextField(max_length=255, null=False)
    lastname = models.TextField(max_length=255, null=False)
    email= models.EmailField(max_length=20,unique=True,null=False)
    number= models.CharField(max_length=15,null=False)
    password=models.CharField(max_length=128)
    confirm_password= models.CharField(max_length=128)
    gender_choices = [
        ("female" , "Feminino"),
        ("male" , "Masculino"),
        ("female", "Feminino"),
        ("others", "Outros"),
        ("none", "Prefiro não dizer")
        ]
    gender = models.CharField(max_length=10, choices=gender_choices)