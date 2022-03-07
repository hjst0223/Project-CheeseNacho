# Generated by Django 3.2.5 on 2022-03-07 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('entmt_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mcomment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mc_title', models.CharField(default='', max_length=30)),
                ('mc_star', models.FloatField()),
                ('mc_content', models.CharField(blank=True, max_length=100)),
                ('mc_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mgenres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Scomment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sc_title', models.CharField(default='', max_length=30)),
                ('sc_star', models.FloatField()),
                ('sc_content', models.CharField(max_length=255)),
                ('sc_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sgenres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sg_genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entmt_info.genres')),
                ('sg_series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entmt_info.series')),
            ],
        ),
    ]
