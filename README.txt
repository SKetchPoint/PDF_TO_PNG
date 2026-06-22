This was designed out of an annoyance of sketchy sites asking for $0.90 or an email... lets just cut to something simple, single file, easy for someone to use. So long as you cd to your folder, this will work on either single or multi pages, havent had any issues with either. Not even a ui as I wanted people to know what they are looking at, be able to read it, and just...have a simple solution to a simple coversion problem. No UI, not a ton of requirements, very few steps. 



COMMAND PROMPT

cd //insert the file path to the folder of the PDFS you want to convert//


IF NOT DONE DO:

winget install oschwartz10612.Poppler


CHECK:

pdftoppm -v


IF NOT DONE DO:

pip install pdf2image


EXECUTION:

python pdf_to_png.py

