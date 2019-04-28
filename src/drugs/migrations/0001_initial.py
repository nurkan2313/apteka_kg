# Generated by Django 2.2 on 2019-04-22 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drugs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.CharField(blank=True, default='', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Stores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=250)),
                ('street_name', models.CharField(blank=True, default='', max_length=250)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('drug', models.ManyToManyField(to='drugs.Drugs')),
            ],
        ),
        migrations.AddField(
            model_name='drugs',
            name='store',
            field=models.ManyToManyField(to='drugs.Stores'),
        ),
    ]