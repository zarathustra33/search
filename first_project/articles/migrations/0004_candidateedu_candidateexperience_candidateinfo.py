# Generated by Django 3.0.5 on 2020-09-17 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateInfo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=264)),
                ('phone_number', models.CharField(max_length=264)),
                ('email', models.EmailField(max_length=254)),
                ('work_experience', models.IntegerField()),
                ('related_work_experience', models.IntegerField()),
                ('leadership_experience', models.IntegerField()),
                ('area_of_focus', models.CharField(max_length=264)),
                ('bytedance_application_position', models.CharField(max_length=264)),
                ('bytedance_application_link', models.URLField()),
                ('linkedin', models.URLField()),
                ('hunter', models.CharField(max_length=264)),
                ('applied_location', models.CharField(max_length=264)),
                ('resume_file', models.FileField(upload_to='')),
                ('location', models.CharField(max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='CandidateExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expid', models.IntegerField()),
                ('start_date', models.CharField(max_length=264)),
                ('end_date', models.CharField(max_length=264)),
                ('company', models.CharField(max_length=264)),
                ('position', models.CharField(max_length=264)),
                ('job_description', models.TextField()),
                ('canid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.CandidateInfo')),
            ],
        ),
        migrations.CreateModel(
            name='CandidateEdu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eduid', models.IntegerField()),
                ('university', models.CharField(max_length=264)),
                ('degree', models.CharField(max_length=264)),
                ('major', models.CharField(max_length=264)),
                ('end_date', models.CharField(max_length=264)),
                ('canid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.CandidateInfo')),
            ],
        ),
    ]
