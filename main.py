from fastapi import FastAPI
from myLib.logic import wiki

res = wiki()
print(res)
