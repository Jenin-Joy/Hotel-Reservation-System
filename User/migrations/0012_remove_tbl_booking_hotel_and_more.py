# Generated by Django 5.0.2 on 2024-04-03 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0011_tbl_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_booking',
            name='hotel',
        ),
        migrations.RemoveField(
            model_name='tbl_booking',
            name='mealpackages',
        ),
        migrations.RemoveField(
            model_name='tbl_booking',
            name='pickanddrophead',
        ),
        migrations.RemoveField(
            model_name='tbl_booking',
            name='roomtype',
        ),
        migrations.RemoveField(
            model_name='tbl_booking',
            name='tourpackages',
        ),
        migrations.RemoveField(
            model_name='tbl_booking',
            name='user',
        ),
        migrations.DeleteModel(
            name='tbl_occupants',
        ),
        migrations.DeleteModel(
            name='tbl_booking',
        ),
    ]
