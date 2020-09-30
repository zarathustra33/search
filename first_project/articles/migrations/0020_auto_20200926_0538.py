# Generated by Django 3.1.1 on 2020-09-26 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('positions', '0003_auto_20200925_0336'),
        ('articles', '0019_auto_20200926_0314'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidateinfo',
            name='applied_company',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='positions.client'),
        ),
        migrations.AddField(
            model_name='candidateinfo',
            name='client_position',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='positions.position'),
        ),
        migrations.AddField(
            model_name='candidateinfo',
            name='flag_experience',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='candidateinfo',
            name='resume_submited_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='candidateinfo',
            name='status',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.DeleteModel(
            name='CandidateStatus',
        ),
    ]