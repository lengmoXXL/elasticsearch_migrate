# elasticsearch_migrate
Migrate elasticsearch Document represented by python into Elasticsearch index

## Requirments

1. django
2. elasticsearch-dsl

## Tutorial

1. install

```
pip install elasticsearch-django-migrate==0.0.1
```

2. Usage

Edit your settings file
```python
DOCUMENT_MIGRATE_APPS = [
    'your app'
]
```

In your app file
```python
from elasticsearch_dsl import Text, Date, Keyword
from elasticsearch_migrate.registry import Document, registry


@registry.register
class Page(Document):
    title = Text(fields={'raw': Keyword()})
    content = Text()
    refreshed_at = Date()

    class Index:
        name = 'page'
```

Notes:
1. `Document` must imported in `elasticsearch_migrate.registry`
2. `name` in `Index` meta must be specified

Then you can use the following commands to migrate

```shell
python manage.py migrate_docs
python manage.py migrate_docs --reindex
```