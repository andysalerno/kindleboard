import os
import logging
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import uvicorn

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="Image Server",
    description="A simple HTTP server that serves an image from the IMAGE_PATH environment variable",
    version="1.0.0",
)


def get_image_path() -> Path:
    """Get the image path from environment variable and validate it exists."""
    image_path_str = os.getenv("IMAGE_PATH")

    if not image_path_str:
        raise HTTPException(
            status_code=500, detail="IMAGE_PATH environment variable is not set"
        )

    image_path = Path(image_path_str)

    if not image_path.exists():
        raise HTTPException(
            status_code=404, detail=f"Image file not found at path: {image_path}"
        )

    if not image_path.is_file():
        raise HTTPException(status_code=400, detail=f"Path is not a file: {image_path}")

    return image_path


def get_media_type(file_path: Path) -> str:
    """Determine the media type based on file extension."""
    suffix = file_path.suffix.lower()
    media_types = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".gif": "image/gif",
        ".bmp": "image/bmp",
        ".webp": "image/webp",
        ".svg": "image/svg+xml",
        ".ico": "image/x-icon",
        ".tiff": "image/tiff",
        ".tif": "image/tiff",
    }
    return media_types.get(suffix, "application/octet-stream")


@app.get("/")
async def root():
    """Root endpoint with basic information."""
    return {
        "message": "Image Server",
        "endpoints": {
            "/image": "GET - Returns the image specified by IMAGE_PATH environment variable",
            "/health": "GET - Health check endpoint",
        },
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    try:
        # Verify that the image path is accessible
        image_path = get_image_path()
        return {
            "status": "healthy",
            "image_path": str(image_path),
            "image_exists": True,
        }
    except HTTPException as e:
        return {"status": "unhealthy", "error": e.detail, "image_exists": False}


@app.get("/image")
async def get_image():
    """Serve the image specified by the IMAGE_PATH environment variable."""
    try:
        image_path = get_image_path()
        media_type = get_media_type(image_path)

        logger.info(f"Serving image: {image_path} with media type: {media_type}")

        return FileResponse(
            path=image_path, media_type=media_type, filename=image_path.name
        )

    except HTTPException:
        # Re-raise HTTP exceptions (they contain appropriate status codes)
        raise
    except Exception as e:
        logger.error(f"Unexpected error serving image: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


def main():
    """Run the server."""
    # Get configuration from environment variables
    host = os.getenv("SERVER_HOST", "127.0.0.1")
    port = int(os.getenv("SERVER_PORT", "8000"))

    logger.info(f"Starting server on {host}:{port}")
    logger.info(f"Image path: {os.getenv('IMAGE_PATH', 'Not set')}")

    uvicorn.run(app, host=host, port=port, log_level="info")


if __name__ == "__main__":
    main()
