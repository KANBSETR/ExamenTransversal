# Generated by Django 5.0.4 on 2024-06-25 17:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('idCargo', models.AutoField(db_column='idCargo', primary_key=True, serialize=False)),
                ('fCreacion', models.DateTimeField(auto_now_add=True)),
                ('nombreCargo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('categorias', models.CharField(choices=[('Vip', 'Vip'), ('Normal', 'Normal'), ('Economico', 'Economico'), ('Familiar', 'Familiar'), ('Suite', 'Suite'), ('Presidencial', 'Presidencial')], default='Normal', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('idComuna', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FormaPago',
            fields=[
                ('idFPago', models.AutoField(db_column='idFPago', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='nombre', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('idGenero', models.AutoField(db_column='idGenero', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='genero', max_length=20)),
                ('fCreacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('idProvincia', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('idRegion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ServicioAdicional',
            fields=[
                ('idServicioAdicional', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=20, unique=True)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('contrasena', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('idHotel', models.AutoField(primary_key=True, serialize=False)),
                ('patenteHotel', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=50)),
                ('estadoHabitacion', models.BooleanField()),
                ('idComuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelVeranum.comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('rut', models.IntegerField(primary_key=True, serialize=False)),
                ('dv', models.CharField(max_length=1)),
                ('nombre', models.CharField(blank=True, max_length=30, null=True)),
                ('apPaterno', models.CharField(blank=True, max_length=30, null=True)),
                ('apMaterno', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('fechaNacimiento', models.DateField(blank=True, db_column='fecha_nacimiento', null=True)),
                ('fCreacion', models.DateTimeField(auto_now_add=True)),
                ('telefono', models.CharField(max_length=15)),
                ('comuna', models.ForeignKey(db_column='idComuna', on_delete=django.db.models.deletion.DO_NOTHING, to='hotelVeranum.comuna')),
                ('genero', models.ForeignKey(db_column='idGenero', on_delete=django.db.models.deletion.DO_NOTHING, to='hotelVeranum.genero')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('idEmpleado', models.AutoField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=20)),
                ('clave', models.CharField(max_length=10)),
                ('sueldo', models.IntegerField()),
                ('fCreacion', models.DateTimeField(auto_now_add=True)),
                ('idCargo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hotelVeranum.cargo')),
                ('rut', models.ForeignKey(db_column='rut', on_delete=django.db.models.deletion.DO_NOTHING, to='hotelVeranum.persona')),
            ],
        ),
        migrations.AddField(
            model_name='comuna',
            name='idProvincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelVeranum.provincia'),
        ),
        migrations.AddField(
            model_name='provincia',
            name='idRegion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelVeranum.region'),
        ),
        migrations.CreateModel(
            name='TipoHabitacion',
            fields=[
                ('idTipoHabitacion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('tiposHabitaciones', models.CharField(choices=[('Simple', 'Simple'), ('Doble', 'Doble'), ('Triple', 'Triple'), ('Matrimonial', 'Matrimonial')], default='Simple', max_length=50)),
                ('idCategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelVeranum.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='HotelDetalle',
            fields=[
                ('idHotelDetalle', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=350)),
                ('cantidadHabitaciones', models.IntegerField()),
                ('cantidadEmpleados', models.IntegerField()),
                ('categoriaHotel', models.CharField(max_length=50)),
                ('idHotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelVeranum.hotel')),
                ('idServicioAdicional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelVeranum.servicioadicional')),
                ('idTipoHabitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelVeranum.tipohabitacion')),
            ],
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('idHabitacion', models.AutoField(primary_key=True, serialize=False)),
                ('numeroHabitacion', models.IntegerField()),
                ('cantDormitorios', models.IntegerField()),
                ('cantBanos', models.IntegerField()),
                ('cantCamas', models.IntegerField()),
                ('tamanoCamas', models.CharField(max_length=50)),
                ('cantPersonasDisp', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('estadoHabitacion', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50, null=True)),
                ('idEmpleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelVeranum.empleado')),
                ('idHotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelVeranum.hotel')),
                ('idServicioAdicional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelVeranum.servicioadicional')),
                ('idTipoHabitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelVeranum.tipohabitacion')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('idReserva', models.AutoField(primary_key=True, serialize=False)),
                ('fechaInicio', models.DateTimeField()),
                ('fechaTermino', models.DateTimeField()),
                ('cantPersonas', models.IntegerField()),
                ('estado', models.BooleanField()),
                ('fCreacion', models.DateTimeField(auto_now_add=True)),
                ('idHabitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelVeranum.habitacion')),
                ('idHotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelVeranum.hotel')),
                ('idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelVeranum.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('idEvento', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('fechaInicio', models.DateTimeField()),
                ('fechaTermino', models.DateTimeField()),
                ('descripcion', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('estado', models.BooleanField()),
                ('fCreacion', models.DateTimeField(auto_now_add=True)),
                ('fModificacion', models.DateTimeField(auto_now=True)),
                ('idEmpleado', models.ForeignKey(db_column='idEmpleado', on_delete=django.db.models.deletion.DO_NOTHING, to='hotelVeranum.empleado')),
                ('idFPago', models.ForeignKey(db_column='idFPago', on_delete=django.db.models.deletion.DO_NOTHING, to='hotelVeranum.formapago')),
                ('idHotel', models.ForeignKey(db_column='idHotel', on_delete=django.db.models.deletion.DO_NOTHING, to='hotelVeranum.hotel')),
                ('idUsuario', models.ForeignKey(db_column='idUsuario', on_delete=django.db.models.deletion.DO_NOTHING, to='hotelVeranum.usuario')),
            ],
        ),
    ]
