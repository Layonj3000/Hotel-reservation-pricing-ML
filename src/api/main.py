from fastapi import FastAPI
from routes.prediction_route import router as prediction_router
from routes.home_route import router as home_router

# Criar uma instância do aplicativo FastAPI
app = FastAPI()

if __name__ == '__main__':
    import uvicorn
    # Executar o servidor Uvicorn com o aplicativo FastAPI
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)
