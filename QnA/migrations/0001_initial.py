# Generated by Django 3.0.14 on 2021-11-17 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo_questions', to='photo.Photo')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=500)),
                ('question', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='QnA.Question')),
            ],
        ),
    ]