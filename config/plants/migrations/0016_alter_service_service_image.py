# Generated by Django 4.1.3 on 2022-12-11 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0015_alter_service_service_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='service_image',
            field=models.ImageField(upload_to='config/plants/files/icon'),
        ),
    ]