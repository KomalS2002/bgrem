# Generated by Django 4.2.1 on 2023-05-22 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0002_remove_imagestoragemodel_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="imagestoragemodel",
            name="downloaded_image",
            field=models.ImageField(blank=True, upload_to="downloads/"),
        ),
    ]