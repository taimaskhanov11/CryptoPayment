from fastapi import FastAPI, Request
from starlette.middleware.trustedhost import TrustedHostMiddleware

app = FastAPI()

# app.add_middleware(
#     TrustedHostMiddleware, allowed_hosts=["193.232.179.110"]
# )


@app.get("/")
async def root(request: Request):
    print(request.url)
    print(await request.body())
    print(request.client)
    return {"message": "Hello World"}


@app.get("/dispatcher")
async def dispatcher(request: Request):
    print(request.client)
    print(await request.body())


@app.post("/dispatcher")
async def dispatcher(request: Request):
    print(request.client)
    print(await request.body())
