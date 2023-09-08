from tkinter import *
import glob
import os
import fitz  # PyMuPDF
from PIL import Image


def pdf2img():
    pdf_name = os.listdir(str(e1.get()))
    #print(pdf_name)

    # Load a document
    all_pdf = glob.glob(str(e1.get()) + "\\*.pdf")
    #print(all_pdf)
    os.chdir(str(e1.get()))

    for i in range(0, len(all_pdf)):
        pdf_path= all_pdf[i]
        # Open the PDF file
        pdf_document = fitz.open(pdf_path)

     # Iterate through each page in the PDF
        for page_number in range(pdf_document.page_count):
            # Get the page
            page = pdf_document.load_page(page_number)

            # Convert the page to an image, dpi is image quality~(100-600)
            image = page.get_pixmap(dpi=300)

            # Create a PIL Image object from the image data
            pil_image = Image.frombytes("RGB", [image.width, image.height], image.samples)
            # Save the image to the output folder
            image_filename = f"{pdf_path[:-4]}.jpg"
            pil_image.save(image_filename)

        # Close the PDF file
        pdf_document.close()


if __name__ == "__main__":
    master = Tk()
    Label(master, text="File Location").grid(row=0, sticky=W)

    e1 = Entry(master)
    e1.grid(row=0, column=1)

    b = Button(master, text="Convert", command=pdf2img)
    b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)

mainloop()


