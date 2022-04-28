from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/success")
async def success(request: Request):
    print(await request.json())


@app.get("/failure")
async def failure(request: Request):
    print(await request.json())


@app.get("/dispatcher")
async def dispatcher(request: Request):
    print(await request.json())


