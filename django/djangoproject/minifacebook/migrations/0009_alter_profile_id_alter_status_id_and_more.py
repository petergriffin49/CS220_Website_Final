# Generated by Django 4.2.11 on 2024-03-27 18:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('minifacebook', '0008_alter_profile_id_alter_status_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='status',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='status',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minifacebook.profile'),
        ),
    ]
