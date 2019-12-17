from elasticsearch_dsl import connections

connections.create_connection(hosts=['index-server-01'])

DOCUMENT_MIGRATE_APPS = [
    'test'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test_migrate',
        'USER': 'test',
        'PASSWORD': 'test',
        'HOST': 'db',
        'PORT': '5432',
    }
}

