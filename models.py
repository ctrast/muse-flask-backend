from peewee import *
from peewee_validates import ModelValidator
import datetime

# Connect to a Postgres database.
DATABASE = PostgresqlDatabase('flask_muse_app', host='localhost', port=5432)


class Song(Model):
    title = CharField(null=False)
    artist = CharField(null=False)
    album = CharField(null=False)
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

obj = Song(code=42)
validator = ModelValidator(obj)
validator.validate()
print(validator.errors)

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Song], safe=True)
    print("TABLES Created")
    DATABASE.close()
