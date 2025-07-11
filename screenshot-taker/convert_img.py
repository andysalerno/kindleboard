from PIL import Image


def convert_image(image_path: str, output_path: str):
    """
    Convert an image to black and white and save it.

    :param image_path: Path to the input image.
    :param output_path: Path where the converted image will be saved.
    """
    img = Image.open(image_path)
    img_bw = img.convert("L")
    img_bw.save(output_path)
