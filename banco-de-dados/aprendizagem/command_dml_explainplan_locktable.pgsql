-- # > Aprendendo Sobre Comandos DML - EXPLAIN PLAN, LOCK TABLE

-- Travando tabelas

-- Permite acesso apenas de leitura

BEGIN;
    LOCK TABLE study.aluno_ada in ACCESS SHARE MODE; 
COMMIT;


-- Permite ver a tabela e suas informações

BEGIN;
    LOCK TABLE study.aluno_ada in ROW SHARE MODE;
COMMIT;


-- Tem a mesma característica que a de cima, porém não permite compartilhamento

BEGIN;
    LOCK TABLE study.aluno_ada in ROW EXCLUSIVE MODE;
COMMIT;


-- # > Utilizando EXPLAIN PLAN - Permite medir a performance da Query no Banco de Dados


EXPLAIN SELECT * FROM study.aluno_ada;

-- Retorno com mais informações

EXPLAIN (FORMAT JSON) SELECT * FROM study.aluno_ada;

-- Analisando a performance de um registro específico

EXPLAIN (FORMAT YAML) SELECT * FROM study.aluno_ada
WHERE id = '1';

-- Medir performance sem a visualização de custos (sem informações desnecessárias)

EXPLAIN (COSTS FALSE) SELECT * FROM study.aluno_ada
WHERE id = '1';

-- Analisando o impacto de um cálculo dentro da tabela

EXPLAIN SELECT MAX(id) FROM
study.aluno_ada WHERE id = '1';