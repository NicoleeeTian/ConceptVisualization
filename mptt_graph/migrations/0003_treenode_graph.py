# Generated by Django 4.1.6 on 2023-02-14 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mptt_graph", "0002_alter_graphmodel_id_alter_treenode_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="treenode",
            name="graph",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="mptt_graph.graphmodel",
            ),
        ),
    ]
