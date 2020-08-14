# Generated by Django 3.0.6 on 2020-06-14 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200613_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='follow_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_from', to='accounts.Profile'),
        ),
        migrations.AlterField(
            model_name='follow',
            name='follow_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_to', to='accounts.Profile'),
        ),
    ]