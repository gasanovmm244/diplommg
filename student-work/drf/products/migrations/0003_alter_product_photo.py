# Generated by Django 5.0.7 on 2024-07-10 18:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_alter_product_articule"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="photo",
            field=models.ImageField(null=True, upload_to="images"),
        ),
    ]