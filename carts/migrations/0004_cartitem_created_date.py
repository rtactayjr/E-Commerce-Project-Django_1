# Generated by Django 4.2.5 on 2023-10-09 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_remove_cartitem_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
