# Generated by Django 5.0.6 on 2024-10-02 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_skill_percent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='percent',
            field=models.IntegerField(max_length=2),
        ),
    ]
