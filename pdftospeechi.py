
import pyttsx3
import PyPDF2
book=open('kk.pdf','rb')
read=PyPDF2.PdfFileReader(book)
pages=read.numPages
print(pages)

speaker=pyttsx3.init()
page=read.getPage(0)
text=page.extractText()
speaker.say(text)
speaker.runAndWait()
