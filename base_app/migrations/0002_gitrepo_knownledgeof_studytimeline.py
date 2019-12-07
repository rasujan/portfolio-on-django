# Generated by Django 2.2.5 on 2019-12-05 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gitrepo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repo_name', models.CharField(max_length=264, unique=True)),
                ('repo_description', models.CharField(max_length=264, unique=True)),
                ('repo_link', models.CharField(max_length=264, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='KnownledgeOf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('framework', models.CharField(max_length=264, unique=True)),
                ('framework_description', models.CharField(max_length=264, unique=True)),
                ('framework_image', models.ImageField(upload_to=None)),
            ],
        ),
        migrations.CreateModel(
            name='studyTimeline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.CharField(max_length=264, unique=True)),
                ('pass_out_year', models.CharField(max_length=264, unique=True)),
                ('degree', models.CharField(max_length=264, unique=True)),
            ],
        ),
    ]
