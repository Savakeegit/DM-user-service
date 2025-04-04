from abc import ABC, abstractmethod

from sqlalchemy import insert, select

from db.database import async_session_maker


class AbstractRepository(ABC):
    @abstractmethod
    async def create_one(self):
        raise NotImplementedError

    @abstractmethod
    async def get_all(self):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def create_one(self, data: dict) -> int:
        async with async_session_maker() as session:
            statement = insert(self.model).values(**data).returning(self.model.id)
            result = await session.execute(statement)
            await session.commit()
            return result.scalar_one()

    async def get_all(self):
        async with async_session_maker() as session:
            statement = select(self.model)
            result = await session.execute(statement)
            result = [row[0].to_row_model() for row in result.all()]
            return result