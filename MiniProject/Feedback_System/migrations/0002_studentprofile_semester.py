# Generated by Django 2.2.5 on 2020-02-27 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Feedback_System', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='semester',
            field=models.CharField(default=1, max_length=1),
        ),
    ]