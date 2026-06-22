COMMAND PROMPT

cd //insert the file path to the folder of the PDFS you want to convert





IF NOT DONE DO:

winget install oschwartz10612.Poppler

CHECK:

pdftoppm -v

IF NOT DONE DO:

pip install pdf2image






EXECUTION:
python pdf_to_png.py


