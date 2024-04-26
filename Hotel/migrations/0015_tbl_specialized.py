# Generated by Django 5.0.2 on 2024-04-02 18:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrator', '0007_tbl_aadhar'),
        ('Guest', '0016_tbl_newhotel'),
        ('Hotel', '0014_remove_tbl_hotelfacility_facility'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_specialized',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_newhotel')),
                ('speci', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administrator.tbl_specification')),
            ],
        ),
    ]