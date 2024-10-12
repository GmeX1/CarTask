import uvicorn
from fastapi import FastAPI

from routers import routers

app = FastAPI()
for router in routers:
    app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app='main:app', host='127.0.0.1', port=8000, reload=True)

# TODO: репозиторий для БД, связь с ручками
