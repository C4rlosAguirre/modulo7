# Generated by Django 4.0.3 on 2022-05-24 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0016_alter_contacto_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name='proveedor',
            name='proveedor',
        ),
        migrations.AddField(
            model_name='proveedor',
            name='direccion',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='familia',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='nombrefantasia',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Contacto'),
        ),
        migrations.CreateModel(
            name='Subfamilia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('proveedor', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='aplicacion.proveedor')),
                ('tienda', models.ManyToManyField(to='aplicacion.tienda')),
            ],
        ),
        migrations.AddField(
            model_name='proveedor',
            name='tienda',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacion.tienda'),
        ),
    ]
