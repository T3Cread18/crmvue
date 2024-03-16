from fastapi import FastAPI
from api.routes import users, customers, orders, products, categories
from api.utils.database import database

app = FastAPI()

# Rutas de la API
app.include_router(users.router)
app.include_router(customers.router)
app.include_router(orders.router)
app.include_router(products.router)
app.include_router(categories.router)

# Conexión y desconexión de la base de datos
@app.on_event("startup")
async def startup_event():
    await database.connect()

@app.on_event("shutdown")
async def shutdown_event():
    await database.disconnect()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)