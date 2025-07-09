from playwright.sync_api import sync_playwright
from playwright.sync_api import Playwright
from pathlib import Path
import os
import time

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "screenshot.png")
URL: str | None = os.environ.get("URL")
UPDATE_SECONDS = 60

if not URL:
    raise ValueError(
        "The environment variable 'URL' must be set to the webpage you want to screenshot."
    )


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

    with sync_playwright() as p:
        while True:
            screenshot_webpage(
                p,
                url=URL,
                viewport_width=1072,
                viewport_height=1448,
                output_path=OUTPUT_PATH,
                device_scale_factor=1.0,
            )

            print("Converting image to black and white...")
            bw_path = OUTPUT_PATH.replace(".png", "_bw.png")
            convert_image(OUTPUT_PATH, bw_path)
            print(f"...Done. Wrote black and white image to: {bw_path}")

            # sleep:
            print(
                f"Waiting {UPDATE_SECONDS} seconds before taking another screenshot..."
            )

            time.sleep(UPDATE_SECONDS)


if __name__ == "__main__":
    main()
