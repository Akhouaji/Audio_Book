import pyttsx3
import PyPDF2

my_pdf = open("Lebenslauf-Akhouajiii.pdf", "rb")
my_pdf_reader = PyPDF2.PdfReader(my_pdf)
pages = len(my_pdf_reader.pages)
print(f"The PDF has {pages} pages. ")


speaker = pyttsx3.init()
for page_num in range(0, pages):
    page = my_pdf_reader.pages[page_num]
    page_text = page.extract_text()
    speaker.say(page_text)
    speaker.runAndWait()