# Generated by Django 4.1.3 on 2022-12-05 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0004_listing_address_line_one_listing_address_line_two_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]
