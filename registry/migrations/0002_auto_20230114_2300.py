# Generated by Django 4.1.5 on 2023-01-15 04:00

from django.db import migrations

def add_default_techs(app, schema):
    Technology = app.get_model('registry','Technology') #con get_models se obtienes varios modelos en una lista
    techs = ['Angular', 'Vue', 'React native', 'CSS', 'Sprintboot', 'Odoo', 'React', 'Flutter', 'Python', 'HTML', 'AWS']
    for tech in techs:
        Technology.objects.create(name = tech).save()

class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0001_initial'),
    ]

    operations = [migrations.RunPython(add_default_techs)
    ]
