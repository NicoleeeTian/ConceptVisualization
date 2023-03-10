# Generated by Django 4.1.6 on 2023-02-13 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mptt_graph", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="graphmodel",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="treenode",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="treenode",
            name="level",
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name="treenode",
            name="lft",
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name="treenode",
            name="rght",
            field=models.PositiveIntegerField(editable=False),
        ),
    ]
