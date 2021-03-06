# Generated by Django 2.2.4 on 2020-03-03 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Feedback_System', '0004_auto_20200301_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='res6',
            field=models.BooleanField(choices=[(5, 'Very Good'), (4, 'Good'), (3, 'Average'), (2, 'Below Average'), (1, 'Poor')], default=False, verbose_name='Punctual to class'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='res7',
            field=models.BooleanField(choices=[(5, 'Very Good'), (4, 'Good'), (3, 'Average'), (2, 'Below Average'), (1, 'Poor')], default=False, verbose_name='Covering Syllabus in time'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='res8',
            field=models.BooleanField(choices=[(5, 'Very Good'), (4, 'Good'), (3, 'Average'), (2, 'Below Average'), (1, 'Poor')], default=False, verbose_name='Sharing additional resources'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='res1',
            field=models.BooleanField(choices=[(5, 'Very Good'), (4, 'Good'), (3, 'Average'), (2, 'Below Average'), (1, 'Poor')], default=False, verbose_name='Clear and Audible voice'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='res2',
            field=models.BooleanField(choices=[(5, 'Very Good'), (4, 'Good'), (3, 'Average'), (2, 'Below Average'), (1, 'Poor')], default=False, verbose_name='Knowledge on Subject'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='res3',
            field=models.BooleanField(choices=[(5, 'Very Good'), (4, 'Good'), (3, 'Average'), (2, 'Below Average'), (1, 'Poor')], default=False, verbose_name='Student Interaction & Doubts Clarification'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='res4',
            field=models.BooleanField(choices=[(5, 'Very Good'), (4, 'Good'), (3, 'Average'), (2, 'Below Average'), (1, 'Poor')], default=False, verbose_name='Discipline and Control over class'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='res5',
            field=models.BooleanField(choices=[(5, 'Very Good'), (4, 'Good'), (3, 'Average'), (2, 'Below Average'), (1, 'Poor')], default=False, verbose_name='Passion & Enthusiasm to teach'),
        ),
    ]
