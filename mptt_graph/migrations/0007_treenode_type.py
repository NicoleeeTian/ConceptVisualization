# Generated by Django 4.1.6 on 2023-02-16 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mptt_graph", "0006_graphmodel_vote_treenode_vote"),
    ]

    operations = [
        migrations.AddField(
            model_name="treenode",
            name="type",
            field=models.CharField(
                choices=[
                    ("Topic", "topic"),
                    ("Example", "example"),
                    ("Attribute", "attribute"),
                    ("Reason", "reason"),
                    ("Theory", "theory"),
                ],
                default="Topic",
                max_length=20,
            ),
        ),
    ]
