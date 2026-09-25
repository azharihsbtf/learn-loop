from fastapi import FastAPI

app = FastAPI(title="Learn Loop")

@app.get("/")
def root():
  return {"status": "learnloop backend placeholder."}