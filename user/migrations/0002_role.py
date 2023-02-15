# Generated by Django 4.1 on 2023-02-15 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('level', models.IntegerField(verbose_name='level')),
                ('permissions', models.ManyToManyField(related_name='permissions', to='auth.permission')),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
            },
        ),
    ]
