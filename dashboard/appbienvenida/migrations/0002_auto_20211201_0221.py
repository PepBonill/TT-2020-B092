# Generated by Django 3.2.7 on 2021-12-01 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appbienvenida', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='correo',
        ),
        migrations.AddField(
            model_name='usuario',
            name='Contrasena',
            field=models.CharField(default='', max_length=45),
        ),
        migrations.AddField(
            model_name='usuario',
            name='Correo',
            field=models.EmailField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='usuario',
            name='Direccion',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='usuario',
            name='Fecha_nacimiento',
            field=models.CharField(default='', max_length=45),
        ),
        migrations.AddField(
            model_name='usuario',
            name='Telefono',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Ap_materno',
            field=models.CharField(default='', max_length=45),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Ap_paterno',
            field=models.CharField(default='', max_length=45),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Nombre',
            field=models.CharField(default='', max_length=45),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id_Usuario',
            field=models.AutoField(default='', primary_key=True, serialize=False),
        ),
    ]