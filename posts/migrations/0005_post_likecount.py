# Generated by Django 4.0.4 on 2022-04-20 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likeCount',
            field=models.IntegerField(blank=True, default=0, verbose_name='like_count'),
        ),
    ]