from database import FORMS
from models import FormSchema
from repository.abstract_repository import MongoRepository


class FormsRepository(MongoRepository):
    model = FORMS
    schema = FormSchema
