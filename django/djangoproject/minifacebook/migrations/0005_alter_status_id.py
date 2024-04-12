# Generated by Django 4.2.11 on 2024-03-27 17:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('minifacebook', '0004_alter_status_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
