# Generated by Django 2.0.9 on 2019-02-24 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='telegram_id',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
