from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from .schema import schema


app = FastAPI(title="GraphQL Server Demo")

graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")


@app.get("/health")
def health():
    return {"status": "ok"}