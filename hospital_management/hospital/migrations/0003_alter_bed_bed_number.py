# Generated by Django 4.2.6 on 2023-10-22 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_alter_room_room_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bed',
            name='bed_number',
            field=models.IntegerField(),
        ),
    ]