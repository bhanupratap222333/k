# Generated by Django 5.0.6 on 2024-06-18 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khanadotcom_app', '0008_remove_menuitem_image_url_menuitem_menu_item_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='availability',
            field=models.BooleanField(default=True),
        ),
    ]