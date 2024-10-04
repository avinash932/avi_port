# Generated by Django 5.0.6 on 2024-10-02 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_project_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='slug',
        ),
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.CharField(default=50, max_length=50),
            preserve_default=False,
        ),
    ]
