from fastapi import FastAPI
import uvicorn
from model import sum_num
import logging


# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/sum")
def add_numbers(a: float, b: float):
    result = sum_num(a,b)
    logger.info(f"application results: {result}")
    return {"sum": result}

# Run the app with: uvicorn main:app --reload
if __name__=='__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)