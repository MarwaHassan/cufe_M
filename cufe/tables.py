import django_tables2 as tables
from cufe.models import CufeUserItems


class UserItemsTable(tables.Table):
    class Meta:
        model = CufeUserItems
        template_name = 'django_tables2/bootstrap.html'