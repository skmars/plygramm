# Generated by Django 4.1.4 on 2022-12-20 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='current_task',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.task'),
        ),
    ]
