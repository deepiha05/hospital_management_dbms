# Generated by Django 4.1.7 on 2023-03-03 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0020_test_treatment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='status',
        ),
    ]