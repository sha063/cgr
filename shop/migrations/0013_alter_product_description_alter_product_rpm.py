# Generated by Django 5.0 on 2023-12-13 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_alter_product_armature_alter_product_brush_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='rpm',
            field=models.FloatField(),
        ),
    ]
