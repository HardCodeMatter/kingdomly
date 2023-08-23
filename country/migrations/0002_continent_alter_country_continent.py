# Generated by Django 4.1 on 2023-02-07 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('area', models.IntegerField(blank=True, null=True, verbose_name='Area')),
            ],
        ),
        migrations.AlterField(
            model_name='country',
            name='continent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='country.continent'),
        ),
    ]
