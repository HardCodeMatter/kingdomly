# Generated by Django 4.1 on 2023-02-15 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0002_continent_alter_country_continent'),
    ]

    operations = [
        migrations.AddField(
            model_name='continent',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='continents', verbose_name='Image'),
        ),
    ]
