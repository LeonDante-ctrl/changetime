# Generated by Django 4.0.2 on 2022-04-02 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('changeapp', '0003_alter_articles_post_moneydonations_articledonations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articledonations',
            name='user',
        ),
    ]
