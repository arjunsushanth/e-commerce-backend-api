# Generated by Django 4.1.3 on 2023-04-01 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='templates/product_images')),
                ('category', models.CharField(choices=[('mobile', 'Mobile'), ('laptop', 'Laptop'), ('tablet', 'Tablet'), ('earphone', 'Ear Phone'), ('earpods', 'Ear Pods'), ('gameing_console', 'Gameing Console')], max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
