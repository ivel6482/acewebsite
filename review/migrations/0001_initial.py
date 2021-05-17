# Generated by Django 2.2.4 on 2019-12-20 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0008_auto_20190821_1515'),
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectionResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField(blank=True)),
                ('rating', models.IntegerField(default=0)),
                ('is_selected', models.TextField(blank=True)),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Submission')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile', verbose_name='Reviewed By')),
            ],
            options={
                'unique_together': {('user', 'submission')},
            },
        ),
    ]