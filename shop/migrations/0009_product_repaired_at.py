# Generated by Django 4.2.7 on 2023-11-27 10:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_rename_name_product_id_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='repaired_at',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
