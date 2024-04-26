# Generated by Django 5.0.2 on 2024-03-05 12:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrator', '0001_initial'),
        ('Guest', '0003_rename_user_addr_tbl_newuser_u_addr'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_newhotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=50)),
                ('hotel_ratings', models.CharField(max_length=50)),
                ('hotel_contact', models.CharField(max_length=50)),
                ('hotel_email', models.CharField(max_length=50)),
                ('hotel_pass', models.CharField(max_length=50)),
                ('hotel_addr', models.CharField(max_length=50)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administrator.tbl_place')),
            ],
        ),
    ]