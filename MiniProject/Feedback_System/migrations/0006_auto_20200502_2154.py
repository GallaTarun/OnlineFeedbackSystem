# Generated by Django 2.2.5 on 2020-05-02 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Feedback_System', '0005_auto_20200303_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='res1',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='res2',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='res3',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='res4',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='res5',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='res6',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='res7',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='res8',
            field=models.CharField(max_length=10),
        ),
    ]