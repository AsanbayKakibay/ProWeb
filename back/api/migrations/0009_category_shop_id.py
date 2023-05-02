# Generated by Django 2.2 on 2022-04-24 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20220424_0530'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='shop_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='api.Shop'),
        ),
    ]
