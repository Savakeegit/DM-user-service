from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
import os

engine = create_async_engine(
    f'postgresql+asyncpg://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@'
    f'{os.environ['DB_HOST']}:{os.environ['DB_PORT']}/{os.environ['DB_NAME']}',
    echo=True,
)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def get_async_session():
    async with async_session_maker() as session:
        yield session