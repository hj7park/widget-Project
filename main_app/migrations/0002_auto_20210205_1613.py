# Generated by Django 3.1.5 on 2021-02-05 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='widget',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='widget',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
