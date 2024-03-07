from fastapi import FastAPI
import schemas


app = FastAPI()



@app.post("/blog")
def create(request:schemas.Blog):
    return request