# Generated by Django 3.0.5 on 2020-09-17 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20200917_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidateinfo',
            name='applied_location',
            field=models.CharField(max_length=264, null=True),
        ),
        migrations.AlterField(
            model_name='candidateinfo',
            name='bytedance_application_link',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='candidateinfo',
            name='leadership_experience',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='candidateinfo',
            name='linkedin',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='candidateinfo',
            name='location',
            field=models.CharField(max_length=264, null=True),
        ),
        migrations.AlterField(
            model_name='candidateinfo',
            name='related_work_experience',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='candidateinfo',
            name='resume_file',
            field=models.FileField(default=None, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='candidateinfo',
            name='work_experience',
            field=models.IntegerField(null=True),
        ),
    ]