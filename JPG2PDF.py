from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
from PIL import Image

# CONVERSIONE 2 PDF

#PDF:
input_directory = "C:\\Users\\scrib\\PycharmProjects\\GiuliaPower\\JPG"
output_directory = "C:\\Users\\scrib\\PycharmProjects\\GiuliaPower\\OUTPUT_PDF"

# Lista dei file nella directory di input
image_files = os.listdir(input_directory)
image_files = [f for f in image_files if f.endswith('.jpg') or f.endswith('.jpeg')]  # Solo file immagine JPG/JPEG

# Creazione del PDF
output_pdf_path = os.path.join(output_directory, 'merged_images.pdf')
c = canvas.Canvas(output_pdf_path, pagesize=letter)

for image_file in image_files:
    image_path = os.path.join(input_directory, image_file)
    img = Image.open(image_path)
    width, height = letter
    img_width, img_height = img.size

    # Calcolo delle dimensioni per adattare l'immagine alla pagina PDF
    aspect_ratio = img_width / img_height
    if aspect_ratio > 1:
        img_width = width - 40
        img_height = img_width / aspect_ratio
    else:
        img_height = height - 40
        img_width = img_height * aspect_ratio

    c.setPageSize((img_width, img_height))
    c.drawImage(image_path, 20, 20, width=img_width, height=img_height)
    c.showPage()

c.save()
print(f"PDF creato con successo: {output_pdf_path}")





















