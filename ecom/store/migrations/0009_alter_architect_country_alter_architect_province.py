# Generated by Django 4.2.5 on 2024-01-15 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_order_face'),
    ]

    operations = [
        migrations.AlterField(
            model_name='architect',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='architect',
            name='province',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
