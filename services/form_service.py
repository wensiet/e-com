import re
from datetime import datetime

from email_validator import validate_email

from models.formschema import GetFormSchema
from repository import FormsRepository


class FormService:
    def __init__(self, repo: FormsRepository):
        self.repository = repo

    async def add_form(self, order):
        await self.repository.add_one(order)

    async def find_form(self, first, second):
        f_name1 = FormService.recognise_field_type(first)
        f_name2 = FormService.recognise_field_type(second)

        filters1 = {
            "field_name_1": f_name1,
            "field_name_2": f_name2
        }

        filters2 = {
            "field_name_1": f_name2,
            "field_name_2": f_name1
        }

        f_req = await self.repository.find_many(filters1)
        s_req = await self.repository.find_many(filters2)

        if f_req is not None:
            return f_req[0]

        if s_req is not None:
            return s_req[0]

        return GetFormSchema(f_name1=first, f_name2=second)

    @staticmethod
    def recognise_field_type(field: str):
        if FormService._valid_date(field):
            return "date"
        if FormService._valid_email(field):
            return "email"
        if FormService._validate_phone(field):
            return "phone"
        return "text"

    @staticmethod
    def _valid_date(v):
        date_formats = ["%d.%m.%Y", "%Y-%m-%d"]
        for date_format in date_formats:
            try:
                datetime.strptime(v, date_format)
                return True
            except ValueError:
                return False
        return False

    @staticmethod
    def _valid_email(v):
        try:
            validate_email(v, check_deliverability=False)
            return True
        except Exception:
            return False

    @staticmethod
    def _validate_phone(v):
        return re.match(r"^\+\d{11}$", v)
