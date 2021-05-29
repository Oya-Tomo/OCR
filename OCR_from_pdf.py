import PyPDF2
from googletrans import Translator

translator = Translator()



with open("E:/program/mbed/HCSR04(距離センサ)/HCSR04.pdf","rb") as f:
  reader = PyPDF2.PdfFileReader(f)
  page = reader.getPage(0)
  print(page.extractText())

  text = translator.translate(text=page.extractText(),dest="ja",src="en").text
  print(text)
