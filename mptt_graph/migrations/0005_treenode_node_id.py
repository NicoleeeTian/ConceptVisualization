# Generated by Django 4.1.6 on 2023-02-14 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mptt_graph", "0004_remove_treenode_graph"),
    ]

    operations = [
        migrations.AddField(
            model_name="treenode",
            name="node_id",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
