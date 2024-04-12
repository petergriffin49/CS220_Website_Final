# Generated by Django 4.2.11 on 2024-03-29 00:46

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('minifacebook', '0009_alter_profile_id_alter_status_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='status',
            name='date_time',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='status',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='status',
            name='message',
            field=models.TextField(db_index=True),
        ),
        migrations.AlterField(
            model_name='status',
            name='profile',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, to='minifacebook.profile'),
        ),
    ]
