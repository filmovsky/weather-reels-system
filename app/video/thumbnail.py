from PIL import Image


def create_thumbnail(input_image: str, output_image: str):

    img = Image.open(input_image)

    img = img.resize((1080, 1920))

    img.save(output_image)

    return output_image