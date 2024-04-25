create table estudiante (
    id_estudiante int primary key,
    nombre varchar(100),
    apellido varchar(100),
    fecha_nacimiento date,
    carrera varchar(100)
);

create table materia (
    id_materia int primary key,
    nombre_materia VARCHAR(100),
    creditos INT
);

create table estudiante_materia (
    id_me int primary key,
    cod_materia int,
    id_estudiante int,
    foreign key (id_estudiante) references estudiante(id_estudiante),
    foreign key (cod_materia) references materia(id_materia)
);

create table notas (
    id_nota int primary key,
    primer_parcial int,
    segundo_parcial int,
    examen_final int,
    cod_materia int,
    id_estudiante int,
    FOREIGN KEY (cod_materia) REFERENCES materia(id_materia),
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante)
);


-- Inserts para la tabla Estudiante
insert into estudiante (id_estudiante, nombre, apellido, fecha_nacimiento, carrera)
values
    (1, 'Leo', 'Loayza', '2000-02-27', 'Sistemas'),
    (2, 'Richard', 'Parra', '2001-05-02', 'Sistemas'),
    (3, 'Angelo', 'Rodriguez', '2004-06-12', 'Sistemas'),
    (4, 'Laura', 'González', '2000-08-12', 'Biología'),
    (5, 'Pedro', 'Rodríguez', '1996-12-03', 'Arquitectura'),
    (6, 'Ana', 'Sánchez', '2001-06-28', 'Psicología');

   -- Inserts para la tabla Estudiante_Materia
insert into estudiante_materia (id_me, cod_materia, id_estudiante)
values
    (1, 1, 1), -- Leo - Base2
    (2, 1, 2), -- Richard - Base2
    (3, 2, 2), -- Richard - S.O
    (4, 3, 3), -- Angelo - Pro4
    (5, 3, 1); -- Leo - Pro4

-- Inserts para la tabla Materia
insert into materia (id_materia, nombre_materia, creditos)
values
    (1,'Base2', 4),
    (2,'S.O', 5),
    (3,'Pro4', 4);

    
-- Inserts para la tabla Notas
insert into Notas (id_nota, primer_parcial, segundo_parcial, examen_final, cod_materia, id_estudiante)
values
    (1, 75, 45, 24, 1, 1), -- Leo - Base2
    (2, 59, 37, 75, 1, 2), -- Richard - Base2
    (3, 35, 95, 65, 2, 2), -- Richard - S.O
    (4, 25, 85, 34, 3, 3), -- Angelo - Pro4
    (5, 12, 78, 36, 3, 1); -- Angelo - Pro4

select * from estudiante
select * from materia 
select * from notas

SELECT e.nombre AS nombre_estudiante, m.nombre_materia, n.primer_parcial, n.segundo_parcial, 
n.examen_final
FROM estudiante e
JOIN estudiante_materia em ON e.id_estudiante = em.id_estudiante
JOIN materia m ON em.cod_materia = m.id_materia
JOIN notas n ON e.id_estudiante = n.id_estudiante AND m.id_materia = n.cod_materia
ORDER BY e.nombre, m.nombre_materia; 

drop table notas 