

## Broker settings.
broker_url = 'amqp://guest:guest@localhost:5672//'

# List of modules to import when the Celery worker starts.
imports = ('cufe.tasks',)

## Using the database to store task state and results.
result_backend = 'django-db'

task_annotations = {'tasks.add': {'rate_limit': '10/s'}}


#CELERY_TIMEZONE = "Australia/Tasmania"
# broker_url = 'pyamqp://'
# result_backend = 'rpc://'
#
# task_serializer = 'json'
# result_serializer = 'json'
# accept_content = ['json']
# timezone = 'Europe/Oslo'
# enable_utc = True


