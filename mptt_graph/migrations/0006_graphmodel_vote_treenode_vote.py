# Generated by Django 4.1.6 on 2023-02-15 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mptt_graph", "0005_treenode_node_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="graphmodel", name="vote", field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="treenode", name="vote", field=models.IntegerField(default=0),
        ),
    ]
