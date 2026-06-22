import os
from pdf2image import convert_from_path

def convert_pdfs_in_folder(folder_path=".", dpi=150):
    # Scan folder for PDF files
    files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]
    
    if not files:
        print("No PDF files found in the directory.")
        return

    for file in files:
        pdf_path = os.path.join(folder_path, file)
        base_name = os.path.splitext(file)[0]
        print(f"Processing: {file}...")
        
        try:
            # Convert PDF pages to PIL Images
            pages = convert_from_path(pdf_path, dpi=dpi)
            
            # Save each page as a PNG
            for i, page in enumerate(pages):
                output_filename = f"{base_name}_page_{i + 1}.png"
                output_path = os.path.join(folder_path, output_filename)
                page.save(output_path, "PNG")
                print(f"  -> Saved: {output_filename}")
                
        except Exception as e:
            print(f"Error processing {file}: {e}")

if __name__ == "__main__":
    # Runs in the current working directory where the script is executed
    convert_pdfs_in_folder()