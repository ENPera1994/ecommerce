# Generated by Django 4.2.5 on 2024-01-15 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_architect_face_product_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='face',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.face'),
        ),
    ]
