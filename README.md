# xy-inc

Projeto para cadastro e recuperação Pontos de Interesse (POI's).

## Como criar o ambiente?

1. Clone o repositório
2. Crie um virtualenv com Python 3.5
3. Ative o seu virtualev.
4. Instale as dependências.
5. Execute os testes.
6. Inicialize os dados de teste.

```console
git clone git@github.com:n1lux/xy-inc.git xyinc
cd xyinc
python -m venv .xyinc
source .xyinc/bin/activate
pip install -r requirements.txt
python manage.py test
python manage.py initial_data
python manage.py collectstatic
```

## Como executar o servidor

```console
python manage.py runserver
```

## Como testar os serviços

### No navegador

#### Para consultar todo os POI's cadastrados
```bash
[GET] http://localhost:8000/api/v0/pois/
```


#### Para criar um poi
```bash
[POST] http://localhost:8000/api/v0/pois/

No campo Media type: application/json

No campo content :
{"name": "teste pois navegador", "x": 45, "y": 20 }
```


#### Para buscar os POI's com base nos parametros informados
```bash
[GET] http://localhost:8000/api/v0/pois/search/?x=20&y=10&d-max=10
```



### Utilizando curl
#### Para consultar todos os POI's cadastrados:
```console
curl -X GET -H "Accept:application/json" http://localhost:8000/api/v0/pois/
```

#### Para criar um poi:
```console
curl -i -X POST -H "Content-Type:application/json" http://localhost:8000/api/v0/pois/ -d '{"name":"teste poi curl", "x": 25, "y": 10}'
```

#### Para buscar os POI's com base nos parametros informados:
```console
curl -X GET -H "Accept:application/json" "http://localhost:8000/api/v0/pois/search/?x=20&y=10&d-max=10"
```

