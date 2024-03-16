import asyncpg
from asyncpg.pool import Pool

class Database:
    def __init__(self, dsn: str):
        self.dsn = dsn
        self.pool = None

    async def connect(self):
        self.pool = await asyncpg.create_pool(dsn=self.dsn)

    async def disconnect(self):
        await self.pool.close()

database = Database(dsn="postgresql://postgres:1234@192.168.175.71/crm")