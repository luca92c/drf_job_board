# Generated by Django 3.0.2 on 2020-01-18 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joboffer',
            name='salary',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
