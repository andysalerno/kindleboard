from playwright.sync_api import sync_playwright
from playwright.sync_api import Playwright
from pathlib import Path
import os
import time

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "screenshot.png")
IMG_WIDTH = int(os.environ.get("IMG_WIDTH", 1072))
IMG_HEIGHT = int(os.environ.get("IMG_HEIGHT", 1448))
UPDATE_SECONDS = int(os.environ.get("SCREENSHOT_INTERVAL", 60))
SCALE_FACTOR = float(os.environ.get("SCALE_FACTOR", 1.0))


def get_url() -> str:
    url = os.environ.get("URL")

    if not url:
        raise ValueError(
            "The environment variable 'URL' must be set to the webpage you want to screenshot."
        )

    return url


def screenshot_webpage(
    playwright: Playwright,
    url: str,
    viewport_width: int,
    viewport_height: int,
    output_path: str,
    device_scale_factor: float = 1.0,
):
    """
    Take a screenshot of a webpage using a headless browser.

    Args:
        url: The URL of the webpage to screenshot
        viewport_width: Width of the browser viewport in pixels
        viewport_height: Height of the browser viewport in pixels
        output_path: Path where the PNG screenshot will be saved
        device_scale_factor: Scale factor for high-DPI displays (e.g., 2.0 for Retina)
                           The final image will be viewport_width * scale x viewport_height * scale
    """
    # Ensure the output directory exists
    output_dir = os.path.dirname(output_path)
    if output_dir:
        Path(output_dir).mkdir(parents=True, exist_ok=True)

    # Launch a headless browser
    browser = playwright.chromium.launch(headless=True)

    # Create a new page with the specified viewport size and scale factor
    page = browser.new_page(
        viewport={"width": viewport_width, "height": viewport_height},
        device_scale_factor=device_scale_factor,
    )

    try:
        page.goto(url, wait_until="networkidle")

        page.screenshot(path=output_path, type="png")

        print(f"Full-color screenshot saved to: {output_path}")

    finally:
        browser.close()


def main():
    from convert_img import convert_image

    TMP_OUTPUT_PATH = OUTPUT_PATH.replace(".png", "_tmp.png")

    with sync_playwright() as p:
        while True:
            screenshot_webpage(
                p,
                url=get_url(),
                viewport_width=IMG_WIDTH,
                viewport_height=IMG_HEIGHT,
                output_path=TMP_OUTPUT_PATH,
                device_scale_factor=SCALE_FACTOR,
            )

            print("Converting image to black and white...")
            convert_image(TMP_OUTPUT_PATH, OUTPUT_PATH, (IMG_WIDTH, IMG_HEIGHT))
            print(f"...Done. Wrote black and white image to: {OUTPUT_PATH}")

            print(
                f"Waiting {UPDATE_SECONDS} seconds before taking another screenshot..."
            )

            time.sleep(UPDATE_SECONDS)


if __name__ == "__main__":
    main()
