# Generated by Django 4.2 on 2024-10-26 02:42

import ckeditor.fields
from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='features',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Cruise Control', 'Cruise Control'), ('Audio Interface', 'Audio Interface'), ('Airbags', 'Airbags'), ('Air Conditioning', 'Air Conditioning'), ('Seat Heating', 'Seat Heating'), ('Alarm System', 'Alarm System'), ('ParkAssist', 'ParkAssist'), ('Power Steering', 'Power Steering'), ('Reversing Camera', 'Reversing Camera'), ('Direct Fuel Injection', 'Direct Fuel Injection'), ('Auto Start/Stop', 'Auto Start/Stop'), ('Wind Deflector', 'Wind Deflector'), ('Bluetooth Handset', 'Bluetooth Handset')], max_length=195),
        ),
    ]
