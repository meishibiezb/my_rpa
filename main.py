import pyautogui
import tkinter as tk
import keyboard
from PIL import Image, ImageTk
import os

canvas = None
root = None
bg_img_id = None
bg_index = 0

def close_window():
    print("关闭窗口")
    root.destroy()

def change_logo(): #换logo
    Da_Image = Image.open("Genshin_PI.png")
    icon = ImageTk.PhotoImage(Da_Image)
    root.iconphoto(False, icon)

def load_image(folder="genshin_img"): #读取图片
    images = []
    original_images = []
    if not os.path.isdir(folder):
        print(f"{folder}文件夹不存在")
        return
    for filename in os.listdir(folder):
        if filename.lower().endswith((".png",".jpg",".jpeg")):
            path = os.path.join(folder, filename)
            try:
                img = Image.open(path)
                img_tk = ImageTk.PhotoImage(img)
                original_images.append(img)
                images.append(img_tk)
                print(f"图片加载成功: {filename}")
            except Exception as e:
                print(f"图片加载失败：{filename}, 错误原因: {e}")
    return images,original_images

def Force_update(original_images):
    global bg_img_id, bg_index
    w = canvas.winfo_screenwidth()
    h = canvas.winfo_screenheight()

    if w < 10: w = root.winfo_screenwidth()
    if h < 10: h = root.winfo_screenheight()

    current_img = original_images[bg_index]
    resized_img = current_img.resize((w, h),Image.Resampling.LANCZOS)
    new_tk = ImageTk.PhotoImage(resized_img)

    canvas.itemconfig(bg_img_id, image=new_tk)
    canvas.bg_img = new_tk

def Realtime_update(event,Da_bg_Image): # 自适应边框大小
    global bg_img_id,bg_index
    new_width, new_height = event.width, event.height
    current_img = Da_bg_Image[bg_index]
    resized = current_img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    new_tk = ImageTk.PhotoImage(resized)
    canvas.itemconfig(bg_img_id, image=new_tk)
    canvas.bg_img = new_tk

def change_bg(images,index,orginals):
    global bg_img_id , bg_index
    bg_index = index
    if not images:
        print("文件夹为空")
        return
    if bg_img_id is None:
        bg_img_id = canvas.create_image(0, 0, anchor="nw")
    Force_update(orginals)

    new_index = (index + 1) % len(images)
    root.after(3000,lambda: change_bg(images,new_index,orginals))

def Create_menu():#菜单
    menu = tk.Menu(root)

    ceshi_menu = tk.Menu(root, tearoff=0)
    ceshi_menu.add_command(label="测试1", command=create_overlay)
    ceshi_menu.add_command(label="测试2", command=create_overlay)
    ceshi_menu.add_command(label="测试3", command=create_overlay)
    ceshi_menu.add_separator()
    ceshi_menu.add_command(label="退出", command=root.destroy)

    settings_menu = tk.Menu(root, tearoff=0)
    settings_menu.add_command(label="切换背景")
    settings_menu.add_command(label="退出",command=root.destroy)

    menu.add_cascade(label="测试", menu=ceshi_menu)
    menu.add_cascade(label="设置", menu=settings_menu)

    root.config(menu=menu)


def create_overlay():
    global canvas,root

    root = tk.Tk()
    root.title("Genshin Impact NB")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}+0+0")

    root.attributes('-topmost', True)
    root.config(bg='gray20')
    root.attributes('-transparentcolor', 'gray20')
    #root.overrideredirect(True)

    canvas = tk.Canvas(root, bg='gray20', highlightthickness=0)
    canvas.pack(expand=True, fill='both')

    w = 400
    h = 400
    border_width = 2
    canvas.create_rectangle(
        border_width, border_width,
        w - border_width, h - border_width,
        outline='lime',
        width=2
    )

    canvas.create_text(w/2, h/2, text="Canvas 画出的边框", fill='white', font=('Arial', 16))

    change_logo()
    #create_bg_img()
    Create_menu()
    Da_images,Da_originals = load_image()
    root.bind("<Configure>", lambda e: Realtime_update(e, Da_originals))

    if Da_images:
        change_bg(Da_images,index=0,orginals = Da_originals)

    keyboard.on_press_key("esc", lambda e: close_window(root))

    root.mainloop()

def main():
    print("Hello from my-rpa!")
    #screenshot = pyautogui.screenshot();
    #screenshot.save("screenshot.png");
    create_overlay()

if __name__ == "__main__":
    main()