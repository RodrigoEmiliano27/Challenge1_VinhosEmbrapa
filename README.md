# Tech Challenger - Grupo 10 - 1MLET24


## Requisitos

- Python 3.6+
- Pip (Python package installer)

## Instalação

1. **Clonar Repositório**:

    ```sh
    git clone https://github.com/RodrigoEmiliano27/Challenge1_VinhosEmbrapa
    ```

2. **Criar ambiente Virtual** (Opcional):

    ```sh
    python -m venv venv
    source venv/bin/activate 
    ```

3. **Instalar as bibliotecas necessárias**:

    ```sh
    pip install -r requirements.txt
    ```
## Execução

Na pasta do projeto, digite:

```
    python app.py
```

## Acessar Documentação SWAGGER

Com o projeto em execução, acesse:

```
    localhost:5000/apidocs
```
### Credenciais de login válidas

Para ter acesso ás rotas é necessário fazer login na aplicação. Utilize as seguintes credenciais para ter acesso ao sistema


| User | senha |
| ------ | -------------- |
| admin | senha |
| guilherme | senha |
| rodrigo | senha |
| yago | senha |



### Como passar o token de acesso no swagger

Após realizar login, você receberá um token de acesso. Para ter acesso ás rotas da aplicação, você deve preencher abrir o menu Authorize como mostrado na figura abaixo.

![campo](./docs/configuração_swagger.png)

No campo **value** insira: 

```
    Bearer {TOKEN RECEBIDO} 
```

Exemplo:

```
    Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxNjg1NTA5NiwianRpIjoiZTZhMDhmZjEtZmM0MS00OTBiLTkwMjctNjg1YzEyMWM0Yjg0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImFkbWluIiwibmJmIjoxNzE2ODU1MDk2LCJjc3JmIjoiNTY5MTdmZmEtMWZjNy00ZmM1LTg5M2UtZGM0NzJjMjFjNTk4IiwiZXhwIjoxNzE2ODU1OTk2fQ.pWJW-nyuCuZMlI4xnHAoA3-ei8B-ZrU3dEs33gne7o0
```



## Arquitetura do modelo

![doc2](https://github.com/RodrigoEmiliano27/Challenge1_VinhosEmbrapa/assets/62484044/d879f30c-fb9c-485f-8618-5ee4020f63b4)

## Diagrama de classes da aplicação

![teste](https://github.com/RodrigoEmiliano27/Challenge1_VinhosEmbrapa/assets/62484044/da283f06-33ec-4494-bb03-cf96c5fd9002)

## Plano de Deploy

![19a9dc90-ee00-45e1-aa3f-24f44ddeb9c5](https://github.com/RodrigoEmiliano27/Challenge1_VinhosEmbrapa/assets/55152520/519bdf7c-7533-44db-bb32-c18b79032092)

## Integrantes do grupo

| Membro | RM |
| ------ | -------------- |
| Guilherme Aparecido Tavares Da Silva | 353804 |
| Lucas Santos Costa | 354552 |
| Raquel Sales de Azevedo | 354159 |
| Rodrigo Emiliano de Oliveira | 353803 |
| Yago José Barros Caetano | 353994 |

