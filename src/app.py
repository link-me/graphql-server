from fastapi import FastAPI
from ariadne.asgi import GraphQL

from .schema import schema


app = FastAPI(title="GraphQL Server Demo")

graphql_app = GraphQL(schema, debug=True)
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)


@app.get("/health")
def health():
    return {"status": "ok"}