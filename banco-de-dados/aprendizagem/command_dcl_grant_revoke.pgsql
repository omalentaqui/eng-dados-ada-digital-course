-- # > Aprendendo Sobre Comandos DCL - GRANT, REVOKE
-- utilizado por admin para permitir ou revogar acessos

-- GRANT

GRANT privilege_list ALL
on nome_tabela
to role_name

CREATE ROLE joe
login
password '123'

CREATE TABLE filmes(
    id int PRIMARY KEY,
    nome varchar(100),
    categoria varchar(100),
    lingua varchar(100)
);

-- Habilitando ao usuário o acesso ao comando 'SELECT' na tabela (visualização)

GRANT SELECT
ON filmes
TO joe;

INSERT INTO filmes(id, nome, categoria, lingua)
VALUES('1', 'indiana jones', 'aventura', 'Inglês');

SELECT * FROM filmes;


-- Habilitando ao usuários acesso a inserções, atualizações e exclusão ao banco (filmes).

GRANT INSERT, UPDATE, DELETE
ON filmes
TO joe;



-- # > Agora iremos revogar o acesso permitido ao usuário anteriormente.

REVOKE SELECT ON filmes FROM joe;