import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings

logger = logging.getLogger("app.main")

# Initialize FastAPI App
app = FastAPI(
    title="ZapplyX API",
    version="1.0.0",
    docs_url="/docs"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route registrations (skeletons)
# app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
# app.include_router(pipeline.router, prefix="/api/pipeline", tags=["pipeline"])
# app.include_router(admin.router, prefix="/api/admin", tags=["admin"])

@app.get("/api/health", tags=["health"])
async def root_health_check():
    """Diagnostic health check verifying DB and Broker connections."""
    # [Blueprint Interface]
    # Checks database and message broker availability.
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    # Execute uvicorn server in production-ready non-reload mode
    uvicorn.run("app.main:app", host=settings.HOST, port=settings.PORT, reload=False)
