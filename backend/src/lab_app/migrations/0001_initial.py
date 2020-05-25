# Generated by Django 3.0.6 on 2020-05-24 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enrollment_app', '0001_initial'),
        ('challenge_app', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('lab_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('lab_number', models.PositiveIntegerField(default=0)),
                ('title', models.CharField(max_length=100)),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
                ('is_visible', models.BooleanField(default=True)),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enrollment_app.Subject')),
            ],
            options={
                'unique_together': {('subject_id', 'lab_number')},
            },
        ),
        migrations.CreateModel(
            name='LabChallenge',
            fields=[
                ('lab_challenge_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('challenge_number', models.PositiveIntegerField(default=0)),
                ('marks', models.PositiveIntegerField(default=10)),
                ('challenge_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challenge_app.Challenge')),
                ('lab_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_app.Lab')),
            ],
            options={
                'unique_together': {('lab_id', 'challenge_id')},
            },
        ),
        migrations.CreateModel(
            name='ProgrammingLanguage',
            fields=[
                ('programming_language_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('programming_language_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LabChallengeProgrammingLanguage',
            fields=[
                ('lab_challenge_programming_language_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('lab_challenge_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_app.LabChallenge')),
                ('programming_language_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_app.ProgrammingLanguage')),
            ],
            options={
                'unique_together': {('lab_challenge_id', 'programming_language_id')},
            },
        ),
    ]