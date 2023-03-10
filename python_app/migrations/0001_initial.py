# Generated by Django 4.1.3 on 2022-12-17 09:06

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Sub_topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_topic', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='tut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('code', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='python_app.language')),
                ('sub_topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='python_app.sub_topic')),
            ],
        ),
    ]
