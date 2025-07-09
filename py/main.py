from PIL import Image


def main():
    img = Image.open("original.png")
    img_bw = img.convert("L")
    img_bw.save("image.png")


if __name__ == "__main__":
    main()
