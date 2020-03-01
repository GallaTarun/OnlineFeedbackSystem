# Generated by Django 2.2.4 on 2020-03-01 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Feedback_System', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teaches',
            name='section',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], default='A', max_length=1),
        ),
        migrations.AddField(
            model_name='teaches',
            name='year',
            field=models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default='1', max_length=1),
        ),
    ]