from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .config import Settings
from .mcp.routes import router as mcp_router

app = FastAPI(
    title="MCP Aha Themes Server",
    description="Model Context Protocol server for exploring Aha! Product workspace themes",
    version="0.1.0"
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include MCP routes
app.include_router(mcp_router, prefix="/mcp", tags=["MCP"])

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
