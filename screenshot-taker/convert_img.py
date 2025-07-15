from PIL import Image


def convert_image(
    image_path: str,
    output_path: str,
    resize: tuple[int, int] | None = None,
) -> None:
    """
    Convert an image to black and white and save it.

    :param image_path: Path to the input image.
    :param output_path: Path where the converted image will be saved.
    """
    img = Image.open(image_path)
    img_bw = img.convert("L")

    (resize_width, resize_height) = resize if resize is not None else (None, None)

    if resize_width is not None and resize_height is not None:
        # only resize if the dimensions are different from the original:
        original_width, original_height = img.size
        if (resize_width != original_width) or (resize_height != original_height):
            img_bw = img_bw.resize((resize_width, resize_height))

    img_bw.save(output_path)
