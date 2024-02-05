import uvicorn
from fastapi import FastAPI, Header
from starlette.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from redis_cache import set_data_in_redis, get_data_from_redis

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.post("/token")
async def token(authorization: str = Header(None)):
    if authorization is None:
        return JSONResponse(status_code=401, content="Unauthorized!")

    set_data_in_redis(f"token", authorization, 900)
    return JSONResponse(status_code=200, content="Authorized!")


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0")
