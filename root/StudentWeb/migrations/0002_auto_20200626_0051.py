# Generated by Django 3.0.7 on 2020-06-25 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StudentWeb', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='pub_date',
            new_name='birth_date',
        ),
    ]
