from fastapi import FastAPI, Depends
from starlette.responses import JSONResponse

from models import FormSchema
from models.formschema import GetFormSchema
from repository import FormsRepository
from services.form_service import FormService

app = FastAPI()

order_service = FormService(FormsRepository())


@app.post("/api/add-order")
async def add_order(schema: FormSchema):
    await order_service.add_form(schema)
    return JSONResponse(status_code=200, content={"msg": "OK"})


@app.post("/api/get_form")
async def get_form(schema: GetFormSchema = Depends()):
    response = await order_service.find_form(schema.f_name1, schema.f_name2)
    return JSONResponse(status_code=200, content=response.model_dump())
