import pyocr
from PIL import Image


image1=Image.open("sample.png")
image1_gry=image1.convert("L")


tools=pyocr.get_available_tools()
print(tools)



tool=tools[0]
name=tool.get_name()

text1=tool.image_to_string(
  image1_gry,
  lang="jpn",
  builder=pyocr.builders.TextBuilder(tesseract_layout=3)
)

print(text1)
