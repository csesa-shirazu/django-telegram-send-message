# Generated by Django 2.0.9 on 2019-02-23 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='hich', upload_to=''),
            preserve_default=False,
        ),
    ]
