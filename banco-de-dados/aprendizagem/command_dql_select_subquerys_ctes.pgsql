-- # > Aprendendo Sobre os Comandos DQL - SELECT, SUBQUERYS e CTEs

CREATE TABLE study.pedidos(
    id serial PRIMARY KEY,
    nome_prato varchar(255) not null,
    preco_prato int not null,
    data_pedido date
);

INSERT INTO study.pedidos(
    nome_prato,
    preco_prato,
    data_pedido
)
VALUES('strogonoff', '19', '2024-06-19');

INSERT INTO study.pedidos(
    nome_prato,
    preco_prato,
    data_pedido
)
VALUES('brasileiro', '15', '2024-06-20');

INSERT INTO study.pedidos(
    nome_prato,
    preco_prato,
    data_pedido
)
VALUES('parmegiana', '30', '2024-06-21');

SELECT * FROM study.pedidos;


-- Sumarizandos os valores de vendas por meses-ano

SELECT 
EXTRACT (MONTH FROM data_pedido) as mes,
EXTRACT (YEAR FROM data_pedido) as ano,
SUM(preco_prato) as total_vendas
FROM study.pedidos
GROUP BY EXTRACT (MONTH FROM data_pedido),
EXTRACT (YEAR FROM data_pedido)
ORDER BY ano, mes;

-- CTE - Realiza cálculos em uma tabela temporária para melhor visualização do código

WITH vendas_por_mes as(

    SELECT
        DATE_PART('month', data_pedido) as mes,
        DATE_PART('year', data_pedido) as ano,
        SUM(preco_prato) as total_vendas,
        AVG(preco_prato) as media_vendas,
        MAX(preco_prato) as max_vendas,
        MIN(preco_prato) as min_vendas

        FROM study.pedidos
        GROUP BY ano, mes

)

SELECT mes, ano, total_vendas, media_vendas from vendas_por_mes
ORDER BY ano, mes;


-- CTE ANINHADAS

WITH departamentos (id, nome) as (
    SELECT 
        departamento.id,
        departamento.nome
        FROM departamento   
),

colaboradores (id, nome, id_depto) as (
    SELECT
        colaborador.id,
        colaborador.nome,
        colaborador.id_depto
        FROM colaborador
        JOIN departamentos on colaborador.id_depto = departamento.id
),

vendas as (id_colaborador, venda_total) as (
    SELECT 
        pedidos1.id_colaborador,
        SUM(preco_total) 
        FROM pedidos1
        JOIN colaboradores on pedidos1.id_colaborador = colaborador.id
        GROUP BY pedidos.id_colaborador
)

SELECT nome, venda_total
FROM vendas
JOIN colaboradores on vendas.id_colaborador = colaborador.id;


-- Trabalhando com SUBQUERYs

SELECT first_name, last_name, salary
fROM employees
WHERE salary > (SELECT max(salary)
                FROM employess
                WHERE first_name = 'Maria'
)