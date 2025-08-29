"""Main entry point for the BidBrief FastAPI application.

This module initialises the FastAPI app, configures middleware and includes
route modules for the different domains (tenders, packs, plans, drafts, etc.).
For now only a health check endpoint is provided.  Additional routers should
be registered in the `include_router` section below.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def create_app() -> FastAPI:
    """Create and configure the FastAPI application.

    Returns
    -------
    FastAPI
        Configured FastAPI application ready to serve.
    """
    app = FastAPI(
        title="BidBrief API",
        description="REST API for the BidBrief platform",
        version="0.1.0",
        openapi_url="/openapi.json",
        docs_url="/docs",
    )

    # Configure CORS.  Adjust `allow_origins` in production.
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Register routers here, for example:
    # from .routers import tenders
    # app.include_router(tenders.router, prefix="/tenders", tags=["Tenders"])

    @app.get("/healthz", tags=["Health"])
    async def healthz() -> dict[str, str]:  # noqa: D401
        """Health check endpoint.

        Returns a simple status message indicating the API is running.
        """
        return {"status": "ok"}

    return app


app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)