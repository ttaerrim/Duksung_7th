# Generated by Django 2.2.1 on 2019-05-24 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tip', '0005_tip_hit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tip',
            name='file',
            field=models.FileField(null=True, upload_to='tip/'),
        ),
    ]
