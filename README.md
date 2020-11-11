# resale_challenge

## Funcionalidades
Gestão completa (listagem, busca, cadastro, edição e exclusão) de Imobiliárias e Imóveis  

## Instalação

### Requisitos:
- Docker
- Docker Compose

Para executar a aplicação, execute o comando:  
```bash
docker-compose up -d
```
OBS: A aplicação necessita das portas 5000 e 3306 disponíveis. Caso não estejam, você pode editar o arquivo `docker-compose.yml` e alterá-las, nos trechos:

```yml
ports:
    - "5000:5000"
```

```yml
ports:
    - "2306:2306"
```

### Utilização
[Documentação OpenAPI](https://app.swaggerhub.com/apis/gabrielcesar95/resale_challenge/1.0.0)  
[Workspace no Insomnia](https://drive.google.com/file/d/15yttZKZAv7jc9vPEFGGeoHon922Qaq-k/view?usp=sharing)