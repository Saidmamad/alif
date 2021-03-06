# Generated by Django 2.1.1 on 2018-09-29 06:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullAddress', models.CharField(help_text='Please enter the full address of the worker...', max_length=200)),
                ('Phone', models.IntegerField(default=0, help_text='Enter your mobile phone with country city codes by excluding the plus sign ')),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StartDate', models.DateField()),
                ('FinishDate', models.DateField(blank=True)),
                ('TypeOfQualification', models.CharField(help_text='ex. Master Degree; Bachelor Degree, etc', max_length=100)),
                ('NameOfOrganisation', models.CharField(help_text='Name of the institution provided the education', max_length=100)),
                ('Address', models.CharField(help_text='Enter the address', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Position', models.CharField(help_text='Enter the position of the worker ', max_length=100)),
                ('StartDate', models.DateField(auto_now=True)),
                ('FinishDate', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Slug', models.SlugField(max_length=200)),
                ('Name', models.CharField(help_text='Name of the worker ', max_length=100)),
                ('Surname', models.CharField(help_text='Surname of the worker ', max_length=100)),
                ('DOB', models.DateField()),
                ('WorkerPhoto', models.ImageField(blank=True, help_text='Photo of the worker. Please make it small befor uploading', upload_to='workersPhoto/')),
                ('Department', models.CharField(choices=[('Department 1', 'Department 1'), ('Department 2', 'Department 2'), ('IT Department', 'IT Department')], help_text='Select from the list', max_length=100)),
                ('JoinDate', models.DateField()),
                ('Sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Not specified', 'Not specified')], help_text='Select from the list...', max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Worker',
                'verbose_name_plural': 'Workers',
            },
        ),
        migrations.AddField(
            model_name='position',
            name='worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workerlist.Workers'),
        ),
        migrations.AddField(
            model_name='education',
            name='worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workerlist.Workers'),
        ),
        migrations.AddField(
            model_name='address',
            name='worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workerlist.Workers'),
        ),
    ]
