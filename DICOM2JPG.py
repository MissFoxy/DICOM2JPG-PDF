import pydicom
from PIL import Image
import numpy as np
import glob
import os

def convert_dicom_to_jpg(input_path, output_path):
    try:
        # Leggi il file DICOM
        dicom = pydicom.dcmread(input_path, force=True)

        # Ottieni i dati dell'immagine dal file DICOM
        img = dicom.pixel_array

        # Normalizza l'immagine per essere compresa tra 0 e 255 (8-bit)
        img_normalized = ((img - img.min()) / (img.max() - img.min())) * 255.0
        img_normalized = img_normalized.astype(np.uint8)

        # Converte i dati dell'immagine in un'immagine PIL
        img_pil = Image.fromarray(img_normalized)

        # Salva l'immagine in formato JPEG
        output_file = os.path.join(output_path, os.path.basename(input_path) + ".jpg")
        img_pil.save(output_file, "JPEG")
        print(f"Conversione completata: {output_file}")
    except Exception as e:
        print(f"Si è verificato un errore durante la conversione: {e}")



#===============================================================#
input_dicom_path = "C:\\Users\\scrib\\PycharmProjects\\GiuliaPower\\INPUT_DICOM"
output_folder_path = "C:\\Users\\scrib\\PycharmProjects\\GiuliaPower\\JPG"
#===============================================================#


# CONVERSIONE IMMAGINI DICOM 2 JPG
medical_files = glob.glob(os.path.join(input_dicom_path, "*"))


def convert_files_in_directory(input_path, output_path):
    medical_files = glob.glob(os.path.join(input_path, "*"))

    for file_or_dir in medical_files:
        if os.path.isdir(file_or_dir):  # Se è una directory, esegui la conversione dei file al suo interno
            convert_files_in_directory(file_or_dir, output_path)
        else:  # Altrimenti, converti il file
            convert_dicom_to_jpg(file_or_dir, output_path)
            print('File Name:', file_or_dir.split("\\")[-1])


for image_input in medical_files:
    #convert_dicom_to_jpg(image_input, output_folder_path)
    print('File Name:', image_input.split("\\")[-1])



convert_files_in_directory(input_dicom_path, output_folder_path)