# Generated by Django 5.0.3 on 2024-03-24 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_posts_company_name_alter_posts_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='more_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='posts',
            name='post_date',
            field=models.DateField(auto_now_add=True, default='test'),
            preserve_default=False,
        ),
    ]