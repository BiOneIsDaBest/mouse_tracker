import tkinter as tk
from PIL import Image, ImageTk

def show_coordinates(event):
    x, y = event.x, event.y
    coordinates_label.config(text=f"X: {x}, Y: {y}")

root = tk.Tk()
root.title("Mouse Coordinate Tracker")

# Thêm icon cho cửa sổ
root.iconbitmap("asset/app_icon.ico")  # Đảm bảo tệp icon có tên là app_icon.ico trong thư mục làm việc

# Tải hình ảnh
image = Image.open("asset/logo.png")  # Tải hình ảnh logo
image = image.resize((100, 100))  # Resize nếu cần thiết
photo = ImageTk.PhotoImage(image)

# Thêm hình ảnh vào cửa sổ
image_label = tk.Label(root, image=photo)
image_label.pack(pady=10)

# Thêm label hiển thị tọa độ
coordinates_label = tk.Label(root, text="Move the mouse inside the window")
coordinates_label.pack(pady=20)

root.bind('<Motion>', show_coordinates)

root.geometry("400x300")
root.mainloop()
