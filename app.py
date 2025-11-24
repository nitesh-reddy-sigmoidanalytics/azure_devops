from fastapi import FastAPI

app=FastAPI()


@app.get("/")
def homepage():
  return "this code is changed again"
