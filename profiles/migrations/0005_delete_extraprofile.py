# Generated by Django 2.2.9 on 2020-01-08 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_extraprofile_matchuseraddress_matchuserphoto_matchuserprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ExtraProfile',
        ),
    ]