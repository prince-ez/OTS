# Generated by Django 5.0.2 on 2024-08-30 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='ans',
            field=models.CharField(max_length=250),
        ),
    ]