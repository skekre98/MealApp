# Generated by Django 3.0.3 on 2020-02-25 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0005_delete_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='lifestyle',
            field=models.DecimalField(decimal_places=1, default=-1.0, max_digits=2),
        ),
    ]