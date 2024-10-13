----------------------------------------------------------------------------------------------------------------------------------------

# Projeto UDP

## 2. Build do projeto
No diretório principal do projeto (`project_udp/`), execute o seguinte comando para construir todos os containers Docker:


docker-compose build

----------------------------------------------------------------------------------------------------------------------------------------

## 2. Executar os containers
Suba todos os containers com o comando:

docker-compose up

Isso irá iniciar os containers, criar a rede necessária para a comunicação e iniciar o envio das mensagens pelo sender e o recebimento pelo receiver.

----------------------------------------------------------------------------------------------------------------------------------------
docker-compose down
----------------------------------------------------------------------------------------------------------------------------------------


docker logs project_udp-sender
docker logs project_udp-receiver
docker logs project_udp-router1


----------------------------------------------------------------------------------------------------------------------------------------