# Generated by Django 3.2 on 2021-04-29 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
