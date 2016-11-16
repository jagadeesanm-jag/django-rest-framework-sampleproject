import uuid
from cassandra.cqlengine import columns

from django_cassandra_engine.models import DjangoCassandraModel

# Django-cassandra_engine module can be used for accessing from the web



from cassandra.cqlengine import models
from uuid import uuid1
from datetime import datetime



#
# class ExampleModel(DjangoCassandraModel):
#     sample_id = columns.UUID(primary_key=True, default=uuid.uuid4)
#     sample_type = columns.Integer(index=True)
#     created_at = columns.DateTime()
#     description = columns.Text(required=False)


class Ticket(models.Model):
    __table_name__ = 'tickets'
    ticket_id = columns.TimeUUID(primary_key=True,default=uuid1())
    status = columns.Integer(default=1,index=True)
    priority = columns.Integer(default=2,index=True)
    subject = columns.Text(required=True)
    content = columns.Text(required=True)
    created_at = columns.DateTime(default=datetime.now, index=True)







