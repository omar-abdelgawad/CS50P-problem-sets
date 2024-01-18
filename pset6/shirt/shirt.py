import sys
from PIL import Image,ImageOps
from os.path import splitext
def valid_extension(extension):
    extensions = [".jpg",".jpeg",".png"]
    if extension.lower() not in extensions:
        return False
    return True

def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    input_image_path = sys.argv[1]
    out_image_path = sys.argv[2]
    input_image_ext = splitext(input_image_path)[-1]
    out_image_ext = splitext(out_image_path)[-1]

    shirt = Image.open("shirt.png")
    if not valid_extension(input_image_ext):
        sys.exit("Invalid input")
    if not valid_extension(out_image_ext):
        sys.exit("Invalid output")
    if input_image_ext != out_image_ext:
        sys.exit("Input and Output have different extensions")
    try:
        input_image = Image.open(input_image_path)
        resized_input = ImageOps.fit(input_image,shirt.size)
        resized_input.paste(shirt,shirt)
        resized_input.save(out_image_path)
    except FileNotFoundError:
        sys.exit(f"Could not read {read_file_path}")


if __name__ == "__main__":
    main()
