# Generated by Django 5.1.3 on 2024-12-09 06:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Category",
            new_name="CategoryStore",
        ),
        migrations.AlterModelOptions(
            name="categorystore",
            options={"verbose_name_plural": "CategoryStore"},
        ),
    ]