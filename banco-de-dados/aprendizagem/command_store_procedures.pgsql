-- # > Aprendendo Sobre Comandos STORE PROCEDURES
-- São comandos para processar uma vez só com uma função - (utilizado em processos repetidos)

CREATE TABLE contas(
    id serial PRIMARY KEY,
    nome varchar(100),
    saldo dec(15, 2) not null
);

alter table public.contas
set schema study;

-- inserir informações

INSERT INTO study.contas (nome, saldo)
VALUES ('carol', '10000');
INSERT INTO study.contas (nome, saldo)
VALUES ('luis', '8000');

SELECT * FROM study.contas;


-- Criando store procedures

create or replace procedure transferencia(
    enviado int,
    recebe int,
    quantidade dec
)
language plpgsql
as $$
begin

-- subtrair a quantidade da conta de quem enviar

update study.contas
set saldo = saldo - quantidade
where id = enviado;

-- adicionando a quantidade na conta de quem recebe

update study.contas
set saldo = saldo + quantidade
where id = recebe;

commit;
end;$$;

CALL transferencia(1,2,1000);
