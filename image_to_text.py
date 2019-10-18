import pytesseract
from PIL import Image,  ImageEnhance, ImageFilter

directory = 'G:/Tesseract-OCR/tesseract'
filekey = "G:\\image.jpg"
from tkinter import *

def insertText():
    #s = "Hello World"
    #text.insert(1.0, s)
    import pytesseract
    from PIL import Image, ImageEnhance, ImageFilter
    pytesseract.pytesseract.tesseract_cmd = directory

    img = Image.open(filekey)
    text = pytesseract.image_to_string(img, lang='eng+rus')
    print(text)
    img.show()
    s = str(text)
    text1.insert(1.0, text)

root = Tk()

text1 = Text(width=60, height=35)
text1.pack()

frame = Frame()
frame.pack()

b_insert = Button(frame, text="Перевод", command=insertText)
b_insert.pack(side=LEFT)

label = Label()
label.pack()


e1 = Entry(width=50)
def insert():
    e1.insert(0,directory)
b = Button(text="Путь к плагину", command=insert)
e1.pack()
b.pack()


e12 = Entry(width=50)
def insert2():
    e12.insert(0,filekey)
b2 = Button(text="Пусть к файлу", command=insert2)
e12.pack()
b2.pack()


insert()
insert2()
root.mainloop()
