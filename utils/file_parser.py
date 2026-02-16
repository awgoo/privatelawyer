import pdfplumber
from PIL import Image
import pytesseract

def parse_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            t = page.extract_text()
            if t:
                text += t + "\n"
    return text


def parse_image(file):
    image = Image.open(file)
    text = pytesseract.image_to_string(image)
    return text


def parse_file(uploaded):

    name = uploaded.name.lower()

    if name.endswith(".pdf"):
        return parse_pdf(uploaded)

    elif name.endswith((".png",".jpg",".jpeg",".webp")):
        return parse_image(uploaded)

    else:
        return uploaded.read().decode("utf-8")
