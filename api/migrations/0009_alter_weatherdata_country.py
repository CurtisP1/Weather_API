# Generated by Django 4.2 on 2023-04-17 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_rename_last_general_lst'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weatherdata',
            name='country',
            field=models.CharField(max_length=30),
        ),
    ]