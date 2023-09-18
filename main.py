import pyqrcode as qr
from PIL import Image
import tkinter as tk
import os


def QR_button_comand():
    input_char = entry.get()
    qrcode = qr.create(content = input_char,error = 'H')
    i = 0
    while os.path.exists(f"qrcd{i}.png"):
        i += 1
    qrcode.png(file = f"qrcd{i}.png", scale = 6)
    img = Image.open(f"qrcd{i}.png")
    img.show()
    os.remove(f"qrcd{i}.png")


root = tk.Tk()
root.title("QRコードの生成")

label = tk.Label(root, text = "QRコードに埋め込みたい文字列を入力してください")
label.grid()

entry = tk.Entry(root)
entry.grid()

QR_btn = tk.Button(root, text = "QRコードを生成する", command = QR_button_comand)
QR_btn.grid()

root.mainloop()
