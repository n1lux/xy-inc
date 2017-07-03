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
```

## Como executar o servidor

```console
python manage.py runserver
```

## Como testar os serviços

### No navedor
http://localhost:8000/api/v0/pois/search/?x=20&y=10&d-max=10

