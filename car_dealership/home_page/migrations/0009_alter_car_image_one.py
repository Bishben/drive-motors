# Generated by Django 3.2.4 on 2021-07-14 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0008_alter_car_image_one'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image_one',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]