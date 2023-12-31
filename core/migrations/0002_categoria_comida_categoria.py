# Generated by Django 4.2.4 on 2023-08-31 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='comida',
            name='categoria',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='core.categoria'),
            preserve_default=False,
        ),
    ]
