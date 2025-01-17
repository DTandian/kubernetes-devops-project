from fastapi import FastAPI
from routes.user import user
from config.openapi import tags_metadata

app = FastAPI(
    title="Users API",
    description="a REST API using python and postgres",
    version="0.0.1",
    openapi_tags=tags_metadata,
)

# " include all routes from user"
app.include_router(user)
