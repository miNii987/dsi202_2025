# Generated by Django 3.2.16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('matcher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ClothingItem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]