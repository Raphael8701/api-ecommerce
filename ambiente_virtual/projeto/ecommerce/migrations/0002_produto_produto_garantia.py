# Generated by Django 3.1.3 on 2020-11-15 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='produto_garantia',
            field=models.CharField(default='1 ano', max_length=80),
        ),
    ]