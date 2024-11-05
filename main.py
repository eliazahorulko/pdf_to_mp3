from gtts import gTTS
import pdfplumber
from pathlib import Path

# Function to convert PDF to MP3 with step-by-step feedback
def pdf_to_mp3(file_path, language='en'):
    # Step 1: Check if the file exists and is a PDF
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        print("[1/4] File found and ready for conversion.")

        # Extract file name without extension for saving the MP3
        file_name = Path(file_path).stem
        print(f"[2/4] The MP3 file will be saved as: {file_name}.mp3")

        # Step 2: Extract text from the PDF file
        print("[3/4] Extracting text from the PDF file...")
        text = ""
        with pdfplumber.open(file_path) as pdf:
            pages = [page.extract_text() for page in pdf.pages if page.extract_text()]
            text = ''.join(pages).replace('\n', '')

        # Step 3: Convert extracted text to MP3
        if text:
            print("[4/4] Converting text to MP3...")
            my_audio = gTTS(text=text, lang=language)
            my_audio.save(f"{file_name}.mp3")
            return f"[+] {file_name}.mp3 has been saved successfully!\n---Enjoy your audio---"
        else:
            return "[!] No text found in the PDF file."
    else:
        return "[!] File does not exist or is not a PDF. Please check the file path."

def main():
    # Replace with the path to your PDF file
    # || Enter there path to pdf.file
    #_||_
    # \/
    file_path = r""
    result = pdf_to_mp3(file_path)
    print(result)

if __name__ == '__main__':
    main()
