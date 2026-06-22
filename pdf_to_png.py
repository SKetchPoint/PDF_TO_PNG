import os
from pdf2image import convert_from_path
# Look to the README for what needs to be on your computer, really only two things you may need to install 
def convert_pdfs_in_folder(folder_path=".", dpi=150):
    # Scan folder for PDF files, please dont do this without cd TuT
    files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]
    
    if not files:
        # Did you navagate to the correct directory? to the correct folder? make sure you do!
        print("No PDF files found in the directory.")
        return

    for file in files:
        pdf_path = os.path.join(folder_path, file)
        base_name = os.path.splitext(file)[0]
        #Debugging, will tell you what files it is/has processed as its doing it 
        print(f"Processing: {file}...")
        
        try:
            # Convert PDF pages to PIL Images
            pages = convert_from_path(pdf_path, dpi=dpi)
            
            # Save each page as a PNG and renames based on the ammount of pages. Same as title but tite_page
            for i, page in enumerate(pages):
                output_filename = f"{base_name}_page_{i + 1}.png"
                output_path = os.path.join(folder_path, output_filename)
                # Actually saved as a png 
                page.save(output_path, "PNG")
                print(f"  -> Saved: {output_filename}")
                
        except Exception as e:
            # if something occures, you find a bug, welcomed to comment or contact me regarding it
            print(f"Error processing {file}: {e}")

if __name__ == "__main__":
    # Runs in the current working directory where the script is executed, sorry no fancy ui
    convert_pdfs_in_folder()
