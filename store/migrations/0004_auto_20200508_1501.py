# Generated by Django 3.0.6 on 2020-05-08 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20200508_0432'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='contat_no',
            new_name='contact_no',
        ),
    ]