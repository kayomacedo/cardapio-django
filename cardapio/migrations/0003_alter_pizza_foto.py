# Generated by Django 5.0.2 on 2024-02-10 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio', '0002_alter_pizza_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='foto',
            field=models.ImageField(upload_to='../static/assets/pizzas/'),
        ),
    ]
