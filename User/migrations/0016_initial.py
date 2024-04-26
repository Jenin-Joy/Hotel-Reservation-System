# Generated by Django 5.0.2 on 2024-04-03 12:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Administrator', '0007_tbl_aadhar'),
        ('Guest', '0016_tbl_newhotel'),
        ('Hotel', '0017_rename_specialized_name_tbl_specialized_speci'),
        ('User', '0015_remove_tbl_occupants_booking_delete_tbl_booking_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField(auto_now_add=True)),
                ('booking_checkin', models.DateField()),
                ('booking_checkout', models.DateField()),
                ('booking_noofguest', models.CharField(max_length=50)),
                ('booking_amount', models.IntegerField(default='0')),
                ('booking_status', models.IntegerField(default='0')),
                ('booking_floor', models.CharField(max_length=50)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_newhotel')),
                ('mealpackages', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Hotel.tbl_mealpackages')),
                ('pickanddrophead', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Hotel.tbl_pickanddrophead')),
                ('roomtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administrator.tbl_roomtype')),
                ('tourpackages', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Hotel.tbl_tourpackages')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_occupants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupants_name', models.CharField(max_length=50)),
                ('occupants_dob', models.DateField()),
                ('occupants_gender', models.CharField(max_length=50)),
                ('occupants_contact', models.CharField(max_length=50)),
                ('occupants_proof', models.FileField(upload_to='Assets/OccupantsProof/')),
                ('occupants_aadhar', models.CharField(max_length=50)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.tbl_booking')),
            ],
        ),
    ]
