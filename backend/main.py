from fastapi import FastAPI
import asyncpg

app = FastAPI()

# Conexión a la base de datos PostgreSQL
DATABASE_URL = "postgresql://postgres:root@localhost/crm"

async def connect_to_db():
    return await asyncpg.connect(DATABASE_URL)

@app.on_event("startup")
async def startup_db_client():
    app.state.db = await connect_to_db()

@app.on_event("shutdown")
async def shutdown_db_client():
    await app.state.db.close()

@app.get("/")
async def read_root():
    return {"message": "Hello, world"}