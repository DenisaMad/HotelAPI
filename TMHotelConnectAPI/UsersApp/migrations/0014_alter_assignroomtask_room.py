# Generated by Django 4.2.7 on 2024-01-07 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("UsersApp", "0013_remove_assignroomtask_task_assignroomtask_tasks"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assignroomtask",
            name="room",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="UsersApp.room",
            ),
        ),
    ]
