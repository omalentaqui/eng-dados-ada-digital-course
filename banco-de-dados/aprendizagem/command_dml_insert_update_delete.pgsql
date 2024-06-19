-- # > Aprendendo sobre os comandos DML - INSERT, UPDATE E DELETE

-- Inserindo dados à uma tabela

INSERT INTO study.aluno_ada(
    nome_aluno,
    cpf,
    email,
    fone,
    data_nascimento
)
VALUES(
    'Douglas',
    '12345678910',
    'douglas@email.com',
    '(13)91234-5678',
    '1994-05-01'
);

    select * from study.aluno_ada;

INSERT INTO study.aluno_ada(
    nome_aluno,
    cpf,
    email,
    fone,
    data_nascimento
)
VALUES(
    'Vanessa',
    '45612378901',
    'vanessa@email.com',
    '(12)99874-1245',
    '1999-07-12'
);


-- Inserindo os dados e recebendo o retorno no OUTPUT utilizando o comando 'RETURNING'

INSERT INTO study.aluno_ada(
    nome_aluno,
    cpf,
    email,
    fone,
    data_nascimento
)
VALUES(
    'Fabio',
    '1243568970',
    'fabio@email.com',
    '(11)98741-1245',
    '1958-09-25'
)
RETURNING *;

-- Inserir links na tabela

CREATE TABLE study.links(
    id serial primary key,
    url varchar(255) not null,
    name varchar(255) not null,
    description varchar(255),
    last_update date
);

INSERT INTO study.links( url, name )
VALUES ('www.postegressqltutorial.com', 'PostegreSQL Tutorial');

SELECT * FROM study.links;


-- Incluindo nome com aspas (Inserir dois apóstrofo ao texto)

INSERT INTO study.links( url, name )
VALUES ('www.links.com', 'Link''s');


-- Atualizando dados de uma tabela utilizando o comando UPDATE

UPDATE study.aluno_ada SET nome_aluno = 'Matheus',
data_nascimento = '2001-03-24'
WHERE nome_aluno = 'Douglas';

-- Atualizando mais de um dado

UPDATE study.aluno_ada SET data_nascimento = '2002-04-19'
WHERE id in (2, 3);

SELECT * FROM study.aluno_ada


-- Excluindo dados de uma tabela

DELETE FROM study.aluno_ada WHERE id = 3;

-- Excluindo dados e tendo o retorno no OUTPUT

DELETE FROM study.aluno_ada WHERE id = 2
RETURNING nome_aluno;

-- Excluindo todos os registros de uma tabela

DELETE FROM study.aluno_ada;

SELECT * FROM study.aluno_ada