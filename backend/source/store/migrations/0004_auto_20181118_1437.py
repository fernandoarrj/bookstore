# Generated by Django 2.1.3 on 2018-11-18 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_store_hsh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='name',
            field=models.CharField(default=None, max_length=120, unique=True),
        ),
    ]
