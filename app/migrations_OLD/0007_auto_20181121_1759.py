# Generated by Django 2.1.1 on 2018-11-21 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_admin_due_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin',
            old_name='Due_date',
            new_name='Due_dates',
        ),
    ]
