# Generated by Django 3.1.2 on 2021-04-01 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20210331_1125'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name', 'first_name'], 'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
    ]
