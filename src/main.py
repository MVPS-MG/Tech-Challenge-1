import logging

from fastapi import FastAPI
from fastapi.routing import iter_route_contexts

from src.routes import router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("uvicorn")

app = FastAPI(title="Churn Prediction API")
app.include_router(router)

for route_context in iter_route_contexts(router.routes):
    route = route_context.original_route
    methods = (
        sorted(route.methods)
        if route is not None and getattr(route, "methods", None)
        else "-"
    )
    logger.info("%s %s", methods, route_context.path)
