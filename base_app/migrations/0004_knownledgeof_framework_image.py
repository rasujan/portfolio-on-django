# Generated by Django 2.2.5 on 2019-12-06 15:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0003_remove_knownledgeof_framework_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='knownledgeof',
            name='framework_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='../static/img'),
            preserve_default=False,
        ),
    ]