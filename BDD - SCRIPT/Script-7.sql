create table estudiantes (
    id_estudiante SERIAL primary key,
    nombre_completo varchar(100),
    fecha_nacimiento date,
    carrera varchar(100)
);

create table materias (
    id_materia SERIAL primary key,
    nombre varchar(100),
    creditos integer
);

create table notas (
    id SERIAL primary key,
    id_estudiante integer references estudiantes(id_estudiante),
    id_materia integer references materias(id_materia),
    nota integer
);
 
select * from estudiantes e 
select * from materias m 
select * from notas n 