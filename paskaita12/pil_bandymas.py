from PIL import Image, ImageFilter

dog = Image.open('dog.jpg')
new_pixel = (0, 0, 0)
new_data = []
for i in range(10000):
    new_data.append(new_pixel)
dog.putdata(new_data)
dog.show()