# Generated by Django 3.0.5 on 2020-05-02 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20200502_1252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order',
            new_name='customer',
        ),
    ]