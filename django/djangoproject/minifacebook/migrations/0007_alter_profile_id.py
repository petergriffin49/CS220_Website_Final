# Generated by Django 4.2.11 on 2024-03-27 18:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('minifacebook', '0006_alter_status_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
