"""
Filename: pdf_page_extractor.py

This script reads a PDF file and creates two new PDF files by extracting specific
pages from the original file. The first output file contains the first page
(front page), and the second output file contains the second page (back page).

Author: Siddharth Kumar (www.siddharthsah.com)
Last Updated: July 28, 2023
"""

from PyPDF2 import PdfFileReader, PdfFileWriter


def extract_pages(pdf_file_path, page_numbers, output_file_path):
    """
    Extracts specific pages from a PDF file and writes them into a new PDF file.

    Args:
        pdf_file_path: The path to the original PDF file.
        page_numbers: A list of page numbers to extract.
        output_file_path: The path to the output PDF file.
    """

    # Load the PDF file
    pdf = PdfFileReader(pdf_file_path)

    # Initialize a PdfFileWriter object
    pdf_writer = PdfFileWriter()

    # Add the specified pages to the PdfFileWriter object
    for page_num in page_numbers:
        pdf_writer.addPage(pdf.getPage(page_num))

    # Write the pages into a new PDF file
    with open(output_file_path, 'wb') as f:
        pdf_writer.write(f)


def main():
    """
    The main function of the script. It calls the `extract_pages` function to
    extract the front and back pages of a PDF file and save them into new PDF files.
    """

    # The path to the PDF file
    pdf_file_path = 'PDF_ID.pdf'
    file_base_name = pdf_file_path.replace('.pdf', '')

    # Page numbers to extract for the front and back pages
    front_pages = [0]  # Front page is the first page
    back_pages = [1]  # Back page is the second page

    # Extract the front and back pages
    extract_pages(pdf_file_path, front_pages, '{0}_FRONT.pdf'.format(file_base_name))
    extract_pages(pdf_file_path, back_pages, '{0}_BACK.pdf'.format(file_base_name))


if __name__ == "__main__":
    main()
