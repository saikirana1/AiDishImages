# from fastapi import FastAPI, BackgroundTasks
# import time

# app = FastAPI()


# def my_background_task(name: str):
#     print(f"Starting task for {name}")
#     time.sleep(5)
#     print(f"Finished task for {name}")
#     return "hi"


# @app.get("/start-task")
# async def start_task(name: str, background_tasks: BackgroundTasks):
#     background_tasks.add_task(my_background_task, name)

#     return {"message": f"Task for {name} started in background!"}


from fastapi import FastAPI
from contextlib import asynccontextmanager

# 🧠 This is our global model variable
ml_models = {}


# ✅ This function handles startup and shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 🚀 STARTUP: Code before 'yield' runs when app starts
    print("🔌 Loading ML model...")
    ml_models["model"] = lambda x: x * 42  # Fake model

    yield  # 👈 Waits here while app is running

    # 📴 SHUTDOWN: Code after 'yield' runs when app stops
    print("❌ Clearing ML model...")
    ml_models.clear()


# 🏁 Pass lifespan to FastAPI
app = FastAPI(lifespan=lifespan)


@app.get("/predict")
async def predict(x: float):
    return {"result": ml_models["model"](x)}
