# Generated by Django 3.1.1 on 2020-09-22 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_auto_20200922_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestlog',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
