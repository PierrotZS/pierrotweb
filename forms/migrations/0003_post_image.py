# Generated by Django 3.1.6 on 2021-02-07 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_post_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='media/images/posts'),
        ),
    ]
