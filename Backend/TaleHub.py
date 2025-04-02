from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
import gemini as gem

app = FastAPI()
#############
# CORS Policy Handling:
origins = ["http://127.0.0.1:5500","http://localhost:5500"]
app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,  # Allows requests from these origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/story/{cat}")
async def get_item(cat):
    story = gem.getStory(cat)
    return {"message": story}

@app.get("/effective")
async def get_effective(data):
    scene = gem.effective("cute")
    return {"message": story}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=7700)
