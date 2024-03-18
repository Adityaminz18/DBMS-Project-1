from fastapi import FastAPI
import schemas


app = FastAPI()



@app.post("/blog")
def create(request:schemas.Blog):
    return request

@app.post("/update")
def update():
    # update the existing blog
    pass

@app.get("/blog")
def get():
    #fetch all the blog from the database
    pass