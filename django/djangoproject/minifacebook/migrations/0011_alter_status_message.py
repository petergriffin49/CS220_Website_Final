# Generated by Django 4.2.11 on 2024-03-29 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minifacebook', '0010_alter_profile_id_alter_status_date_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='message',
            field=models.TextField(),
        ),
    ]
