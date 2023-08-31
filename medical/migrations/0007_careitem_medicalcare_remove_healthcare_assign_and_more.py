# Generated by Django 4.2.4 on 2023-08-29 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0005_claim_suspension_subscriber_alter_decease_subscriber_and_more'),
        ('medical', '0006_practitioner_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='CareItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplied_at', models.DateField(auto_now_add=True, verbose_name='Supply Date')),
                ('quantity', models.PositiveSmallIntegerField(default=0)),
                ('unit_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('create_at', models.DateField(auto_now_add=True, verbose_name='Creation Date')),
                ('modified_at', models.DateField(auto_now=True, verbose_name='Modified Date')),
                ('note', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalCare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_reference', models.CharField(blank=True, max_length=24, null=True, verbose_name='Doc. Reference')),
                ('create_at', models.DateField(auto_now_add=True, verbose_name='Creation Date')),
                ('modified_at', models.DateField(auto_now=True, verbose_name='Modified Date')),
                ('note', models.TextField(blank=True, null=True)),
                ('assign', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='insurance.assign')),
                ('mr_center', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='medical.healthcenter')),
                ('pathology', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='medical.pathology')),
                ('subscriber', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='insurance.subscriber')),
            ],
        ),
        migrations.RemoveField(
            model_name='healthcare',
            name='assign',
        ),
        migrations.RemoveField(
            model_name='healthcare',
            name='mr_center',
        ),
        migrations.RemoveField(
            model_name='healthcare',
            name='pathology',
        ),
        migrations.RemoveField(
            model_name='healthcare',
            name='staff',
        ),
        migrations.RemoveField(
            model_name='healthcare',
            name='subscriber',
        ),
        migrations.DeleteModel(
            name='HealthCareItem',
        ),
        migrations.AddField(
            model_name='careitem',
            name='healthcare',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='medical.medicalcare'),
        ),
        migrations.AddField(
            model_name='careitem',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='medical.service'),
        ),
        migrations.AddField(
            model_name='careitem',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='medical.staff'),
        ),
        migrations.AlterField(
            model_name='medicationitem',
            name='healthcare',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='medical.medicalcare'),
        ),
        migrations.DeleteModel(
            name='HealthCare',
        ),
    ]