from abc import ABC, abstractmethod
from bson import ObjectId
from pydantic import BaseModel
from fastapi.exceptions import HTTPException


class AbstractRepository(ABC):
    @abstractmethod
    async def get_by_id(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def find_many(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def delete_by_id(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def add_one(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def delete_many(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def update_one(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def update_many(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def get_id(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def push_one(self, *args, **kwargs):
        raise NotImplementedError


class MongoRepository(AbstractRepository):
    model: None
    schema: None

    async def get_by_id(self, doc_id: str):
        if ObjectId.is_valid(doc_id):
            cursor = self.model.find({"_id": ObjectId(doc_id)})
            document = await cursor.to_list(length=None)
            if document:
                return self.schema(**document[0])
        else:
            raise HTTPException(status_code=400, detail="Invalid ID")

    async def find_many(self, filters: dict = None):
        cursor = self.model.find(filters)
        documents = await cursor.to_list(length=None)
        if documents:
            return [self.schema(**document) for document in documents]
        else:
            return None

    async def add_one(self, add_schema: BaseModel = None):
        main_schema = self.schema(**add_schema.model_dump(), _id=None)

        result = await self.model.insert_one(main_schema.dict())
        return str(result.inserted_id)

    async def delete_by_id(self, doc_id: str = None, filters: dict = None):
        self.model.delete_one({"_id": ObjectId(doc_id)})

    async def delete_many(self, filters: dict = None, approve=False):
        if not filters:
            if not approve:
                raise Exception("BY CALLING THIS METHOD YOU ARE GOING TO DROP COLLECTION")
            else:
                await self.model.drop()
        else:
            await self.model.delete_one(filters)

    async def update_one(self, doc_id: str, update_data: dict):
        await self.model.update_one({"_id": ObjectId(doc_id)}, {"$set": update_data})

    async def update_many(self, filters: dict, update_data: dict):
        await self.model.update_many(filters, {"$set": update_data})

    async def get_id(self, schema: BaseModel):
        search_query = schema.model_dump(exclude_unset=True)
        document = await self.model.find_one(search_query)
        if document:
            return str(document["_id"])
        else:
            return None

    async def push_one(self, doc_id: str, element: dict):
        await self.model.update_one({"_id": ObjectId(doc_id)}, {"$push": element})
