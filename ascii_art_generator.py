from PIL  import Image
import os

ASCII_CHARS = "@%#$§÷"
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    COLORAMA= True
except ImportError:
    COLORAMA= False


def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height/width
    new_height = int(aspect_ratio * new_width * 0.55)
    resized_image = image.resize((new_width, new_height), resample=Image.Resampling.LANCZOS)
    return resized_image
def grayify(image):
    return image.convert("L")
def pixels_to_ascii(image):
    pixels = image.getdata()
    chars = "".join([ASCII_CHARS[pixel * len(ASCII_CHARS) // 256] for pixel in pixels])
    return chars

def convert_to_ascii(image_path, new_width=100):
    try:
        image= Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image: {e}")
        return
    image = resize_image(image, new_width)
    ascii_image = pixels_to_ascii(grayify(image))
    pixel_count = len(ascii_image)
    ascii_image= "\n".join([ascii_image[i:i+new_width] for i in range(0, pixel_count, new_width)])

    return ascii_image
def color_ascii(image_path, new_width=100):
    if not COLORAMA:
        print("Colorama not installed, running without colors.")
        return convert_to_ascii(image_path, new_width)
    try:
        image = Image.open(image_path).convert("RGB")
    except Exception as e:
        print(f"Unable to open image: {e}")
        return 
    image = resize_image(image, new_width)
    width, height=image.size
    ascii_str = ""

    for y in range(height):
        for x in range(width):
            r,g,b = image.getpixel((x,y))
            gray_value = int((r+g+b)/3)
            char = ASCII_CHARS[gray_value * len(ASCII_CHARS)//256]
            ascii_str += f"\033[38;2;{r};{g};{b}m{char}\033[0m"
        ascii_str+="\n"
    return ascii_str

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Convert images to ASCII art.")
    parser.add_argument("image", help="Path to the image file")
    parser.add_argument("--width", type=int, default=100, help="Width of ASCII output")
    parser.add_argument("--color", action="store_true", help="Enable colored output")
    args = parser.parse_args()

    if args.color:
        ascii_art = color_ascii(args.image, args.width)
    else:
        ascii_art = convert_to_ascii(args.image, args.width)

    print(ascii_art)

    with open("ascii_output.txt", "w") as f:
        f.write(ascii_art)
