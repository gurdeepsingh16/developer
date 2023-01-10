# Generated by Django 4.1.3 on 2022-12-20 09:08

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('python_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='practice_set',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.CharField(max_length=255)),
                ('program', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='tut',
            name='language',
            field=models.ForeignKey(default='Python', on_delete=django.db.models.deletion.CASCADE, to='python_app.language'),
        ),
        migrations.AlterField(
            model_name='tut',
            name='sub_topic',
            field=models.ForeignKey(default='python', on_delete=django.db.models.deletion.CASCADE, to='python_app.sub_topic'),
        ),
    ]
