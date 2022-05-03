from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def root(request: Request):
    print(request.url)
    print(await request.body())
    return {"message": "Hello World"}


@app.get("/success")
async def success(request: Request):
    print(request.url)
    print(await request.body())
    # print(await request.json())


@app.get("/failure")
async def failure(request: Request):
    print(await request.body())
    # print(await request.json())


@app.get("/dispatcher")
async def dispatcher(request: Request):
    print(await request.body())
    # print(await request.json())

@app.post("/dispatcher")
async def dispatcher(request: Request):
    print(await request.body())
    # print(await request.json())


