# Generated by Django 4.1 on 2022-09-02 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_customuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
