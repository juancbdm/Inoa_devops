# Desafio Inoa DevOps/Infra
Repositório para o desafio de DevOps/Infra da Inoa com objetivo final de receber uma string via GET de uma aplicação em Python.

# Estrutura
Para estrutura escolhi **Postgres** como DB e **Traefik** como reverse-proxy.
![Inoa DevOps/Infra diagrama](https://github.com/juancbdm/Inoa_devops/blob/main/diagram.jpg?raw=true)

# Aplicação em Python
Aplicação simples com 2 metodos, um POST para inserção de dados e outro GET para recebimento das informações.

# Do zero ao "Olá Inoa"
Para automatização de todo processo algumas dependencias precisam estar instaladas:
- [curl](https://curl.se/)
- [jq](https://stedolan.github.io/jq/)
- [Docker](https://docs.docker.com/engine/install/ubuntu/)
- [Docker Compose](https://docs.docker.com/engine/install/ubuntu/)

Tendo essas dependências instaladas, basta performar o comando: ```./setup.sh```

## Variaveis de ambiente
Como o objetivo desse desafio é de chegar ao resultado final com um script simples, esta embarcado o arquivo ```.env```, o que não é uma boa prática para ambientes fora de desenvolvimento.
