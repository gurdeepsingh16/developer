# Generated by Django 4.1.3 on 2023-01-12 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0009_remove_paper_level'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Level',
        ),
    ]