from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
async def Bienvenue():
    try:
        return{"message":"Bonjour Maniche le champion"}
    except Exception as e:
        raise HTTPException(status_code=500, detail= str(e))

@app.get("/test")
async def Bonjour():
    try:
        return{"message":"Bonjour RCW 1002 de serveur"}
    except Exception as e:
        raise HTTPException(status_code=500, detail= str(e))    