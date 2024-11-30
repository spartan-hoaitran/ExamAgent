import uvicorn
from routers.app import api

if __name__ == "__main__":
    uvicorn.run("main:api", host="0.0.0.0", port=8000)
    