# Generated by Django 5.0.2 on 2024-04-01 12:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0013_delete_tbl_floor'),
        ('User', '0005_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_booking',
            name='mealpackages',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Hotel.tbl_mealpackages'),
        ),
        migrations.AlterField(
            model_name='tbl_booking',
            name='pickanddrophead',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Hotel.tbl_pickanddrophead'),
        ),
        migrations.AlterField(
            model_name='tbl_booking',
            name='tourpackages',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Hotel.tbl_tourpackages'),
        ),
    ]