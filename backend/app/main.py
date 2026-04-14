from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models, database
from .routes import auth, loan

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# ✅ CORS setup (important for React connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Include routes
app.include_router(auth.router)
app.include_router(loan.router)
