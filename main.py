from fastapi import FastAPI
import uvicorn
from myLib.logic import wiki as wikilogic
from myLib.logic import pharse as wikipharse
from myLib.logic import search_wiki


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Wiki API call. Call /search or /wiki"}


@app.get("/search/{value}")
async def search(value: str):
    """Page to search"""

    result = search_wiki(value)
    return {"result": result}


@app.get("/wiki/{name}")
async def wiki_search(name: str):
    """Content to Search"""
    res = wikilogic(name)
    return {"res": res}


@app.get("/phrases/{val}")
async def phrases(val: str):
    """Print the phrases"""
    res = wikipharse(val)
    return {"res": res}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
