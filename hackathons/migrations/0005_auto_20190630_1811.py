# Generated by Django 2.1.1 on 2019-06-30 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hackathons', '0004_auto_20190630_1752'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sponsorship',
            old_name='tiers',
            new_name='tier',
        ),
    ]
