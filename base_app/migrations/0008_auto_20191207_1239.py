# Generated by Django 2.2.5 on 2019-12-07 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0007_auto_20191207_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knownledgeof',
            name='framework_image',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]