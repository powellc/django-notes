from django.db.models import Manager

class PublicManager(Manager):
    def get_query_set(self):
        return super(PublicManager, self).get_query_set().filter(public=True)
