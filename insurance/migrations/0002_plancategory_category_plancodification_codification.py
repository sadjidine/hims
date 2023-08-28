# Generated by Django 4.2.4 on 2023-08-26 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0001_initial'),
        ('insurance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plancategory',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.RESTRICT, to='medical.medicinecategory'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plancodification',
            name='codification',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.RESTRICT, to='medical.codification'),
            preserve_default=False,
        ),
    ]