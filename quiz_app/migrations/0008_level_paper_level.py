# Generated by Django 4.1.3 on 2023-01-12 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0007_delete_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='paper',
            name='level',
            field=models.ForeignKey(blank=True, default='Easy', null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz_app.level'),
        ),
    ]
