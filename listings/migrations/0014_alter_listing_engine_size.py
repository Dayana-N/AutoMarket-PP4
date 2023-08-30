# Generated by Django 3.2.20 on 2023-08-30 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0013_auto_20230828_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='engine_size',
            field=models.CharField(choices=[('0.8', '0.8 L'), ('1.0', '1.0 L'), ('1.2', '1.2 L'), ('1.4', '1.4 L'), ('1.6', '1.6 L'), ('1.8', '1.8 L'), ('2.0', '2.0 L'), ('2.2', '2.2 L'), ('2.4', '2.4 L'), ('2.5', '2.5 L'), ('3.0', '3.0 L'), ('3.5', '3.5 L'), ('4.0', '4.0 L'), ('4.2', '4.2 L'), ('4.6', '4.6 L'), ('5.0', '5.0 L'), ('5.5', '5.5 L'), ('6.0', '6.0 L'), ('6.2', '6.2 L'), ('7.0', '7.0 L')], default=2.0, max_length=20),
            preserve_default=False,
        ),
    ]
