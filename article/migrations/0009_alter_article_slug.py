# Generated by Django 3.2.6 on 2021-08-29 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]