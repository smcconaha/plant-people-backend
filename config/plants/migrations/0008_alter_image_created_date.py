# Generated by Django 4.1.3 on 2022-12-07 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0007_alter_listing_created_date_alter_listing_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
