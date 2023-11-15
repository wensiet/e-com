from bson import ObjectId
from pydantic import BaseModel


class FormSchema(BaseModel):
    _id: ObjectId = None
    name: str
    field_name_1: str
    field_name_2: str


class GetFormSchema(BaseModel):
    f_name1: str
    f_name2: str
