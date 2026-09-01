from src.routes.churn import router as churn_router
from src.routes.health import router as health_router

from fastapi import APIRouter

router = APIRouter()

router.include_router(churn_router, tags=["Churn Prediction"])
router.include_router(health_router, tags=["Health Check"])
