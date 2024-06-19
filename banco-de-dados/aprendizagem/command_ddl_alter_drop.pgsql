-- # > Aprendendo a utilizar comandos DDL - ALTER e DROP

alter table study.alunos rename to aluno_ada;

alter table study.aluno_ada rename nome to nome_aluno;

select * from study.aluno_ada;

alter table study.aluno_ada
add teste int;

alter table study.aluno_ada
alter column teste type varchar(255);


-- drop column

alter table study.aluno_ada
drop column teste;


-- criando um novo schema e incluindo uma tabela já criada anteriormente

create schema teste;

alter table study.aluno_ada
set schema teste;

-- deletar a tabela criada

drop table teste.aluno_ada; -- Não foi deletado, pois há dependências de FK em outras telas