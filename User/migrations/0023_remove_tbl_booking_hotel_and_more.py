# Generated by Django 5.0.4 on 2024-04-26 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0022_tbl_booking_no_of_rooms'),
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
            name='tourpackages',
        ),
        migrations.RemoveField(
            model_name='tbl_booking',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tbl_occupants',
            name='booking',
        ),
        migrations.DeleteModel(
            name='roombooking',
        ),
        migrations.DeleteModel(
            name='tbl_booking',
        ),
        migrations.DeleteModel(
            name='tbl_occupants',
        ),
    ]
