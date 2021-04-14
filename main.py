import pyttsx3
import PyPDF2

book=open('10.1.1.23.9764.pdf','rb')
PdfReader=PyPDF2.PdfFileReader(book)
pages=PdfReader.numPages
print(pages)

speaker=pyttsx3.init()
for num in range(0,pages):
    page= PdfReader.getPage(num)
    text=page.extractText()
    speaker.say(text)
    speaker.runAndWait()
