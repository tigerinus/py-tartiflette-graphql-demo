import os

from aiohttp import web
from tartiflette_aiohttp import register_graphql_handlers


def run() -> None:
    """
    Entry point of the application.
    """
    web.run_app(
        register_graphql_handlers(
            app=web.Application(),
            engine_sdl=os.path.dirname(os.path.abspath(__file__)) + "/schema",
            engine_modules=[
                "server.resolvers"
            ],
            executor_http_endpoint="/graphql",
            executor_http_methods=["POST"],
            graphiql_enabled=True,
            subscription_ws_endpoint="/ws",
        )
    )
