# Generated by Django 3.2.8 on 2021-10-20 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pulls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='id',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
