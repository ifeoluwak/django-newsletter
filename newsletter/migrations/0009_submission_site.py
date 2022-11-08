# Generated by Django 3.1.5 on 2021-01-11 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('newsletter', '0008_longer_subscription_name'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='newsletter',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='submission',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site', verbose_name='Site for this submission'),
        ),
    ]