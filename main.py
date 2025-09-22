import pyttsx3
import PyPDF2
import os

def pdf_to_speech(pdf_path, output_path="output/output.mp3"):
    if not os.path.exists(pdf_path):
        print(f"❌ File not found: {pdf_path}")
        return

    pdfreader = PyPDF2.PdfReader(pdf_path)
    pages = len(pdfreader.pages)

    all_text = ""
    for num in range(pages):
        page = pdfreader.pages[num]
        text = page.extract_text()
        if text:
            all_text += text + " "

    if not all_text.strip():
        print("❌ No text found in PDF.")
        return

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    player = pyttsx3.init()
    player.save_to_file(all_text, output_path)
    player.runAndWait()

    print(f"✅ Audio saved to: {output_path}")

if __name__ == "__main__":
    pdf_path = "samples/example.pdf"
    pdf_to_speech(pdf_path)
