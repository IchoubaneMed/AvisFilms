# Generated by Django 5.0.6 on 2024-05-17 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='grad',
            new_name='grade',
        ),
    ]
