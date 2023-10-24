# Generated by Django 4.2.4 on 2023-10-23 10:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('insurance', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]