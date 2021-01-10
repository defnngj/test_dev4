# Generated by Django 3.1.2 on 2021-01-10 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task_manage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='名称')),
                ('error', models.IntegerField(verbose_name='错误用例')),
                ('failure', models.IntegerField(verbose_name='失败用例')),
                ('skipped', models.IntegerField(verbose_name='跳过用例')),
                ('tests', models.IntegerField(verbose_name='总用例数')),
                ('run_time', models.FloatField(verbose_name='运行时长')),
                ('result', models.FilePathField(verbose_name='文件路径')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_manage.task')),
            ],
        ),
    ]
