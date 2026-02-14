ASCII Art Generator

Convert any image into ASCII art in your terminal—grayscale, basic color, or full RGB! Perfect for showing off code + art skills. 🎨💻

Features

Resize images to fit your terminal width

Convert to ASCII characters from dark (@) to light ( )

Optional colored output:

Basic RGB highlights

Full RGB terminal rendering (true color!)

Save output to ascii_output.txt for sharing

Works with Python 3.10+ and Pillow 10+

--Installation--

1- Clone the repo:

git clone https://github.com/gokmendinc/ascii-art-generator.git
cd ascii-art-generator

2- Create a virtual environment (recommended):

python3 -m venv venv
source venv/bin/activate

3- Install dependencies:

pip install -r requirements.txt

Or manually:

pip install pillow colorama

4- Usage
python3 ascii_art_generator.py IMAGE_PATH [--width WIDTH] [--color] [--rgb]


IMAGE_PATH → path to your image file

--width WIDTH → adjust output width (default: 100)

--color → basic colored ASCII output

--rgb → full RGB true color output

Example:

python3 ascii_art_generator.py "my_photo.jpg" --width 80 --color
python3 ascii_art_generator.py "my_photo.jpg" --width 100 --rgb

How it works

Image is resized for terminal display

Converted to grayscale

Each pixel’s brightness mapped to an ASCII character (@, #, ., etc.)

Optional: color applied per pixel using ANSI codes

Output printed in terminal and saved to a file

Tips

For best results, use images with good contrast

Terminal must support ANSI escape codes for colored output

Use quotes around image paths with spaces, e.g.:

python3 ascii_art_generator.py "My Images/photo.jpg"

(Or run with --rgb for full color)

License

MIT License – feel free to tweak, share, and create art 💖
