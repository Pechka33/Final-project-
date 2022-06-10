from tkinter import Button, Tk
from PIL import Image, ImageFilter

main = Tk()
main.title("Foto redactor")
main.geometry('500x500')


def contour():
    img = Image.open('car.jpg')
    newImg = img.filter(ImageFilter.CONTOUR)
    newImg.show()


def blur():
    img = Image.open('car.jpg')
    newImg = img.filter(ImageFilter.BLUR)
    newImg.show()


def secret():
    img = Image.open('car.jpg')
    newImg = img.filter(ImageFilter.SMOOTH)
    newImg2 = newImg.filter(ImageFilter.CONTOUR)
    newImg2.show()


btn1 = Button(
    text="Contour",
    bg='red',
    fg='white',
    command=contour
)

btn2 = Button(
    text="Blur",
    bg='red',
    fg='white',
    command=blur
)

btn3 = Button(
    text="Secret filter",
    bg='red',
    fg='white',
    command=secret
)

btn1.place(relx=0, rely=0, relheight=0.5, relwidth=1)
btn2.place(relx=0, rely=0.5, relheight=0.5, relwidth=0.5)
btn3.place(relx=0.5, rely=0.5, relheight=0.5, relwidth=0.5)
main.mainloop()
