# Generated by Django 4.1.3 on 2022-11-13 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestiarium', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='creatures',
            name='image',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
