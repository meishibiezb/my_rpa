import pyautogui
import tkinter as tk
import keyboard
from PIL import Image, ImageTk

def create_overlay():
    root = tk.Tk()
    root.title("Genshin Impact NB")

    Da_Image = Image.open("Genshin_PI.png")#换图标
    icon = ImageTk.PhotoImage(Da_Image)
    root.iconphoto(False, icon)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}+0+0")
    
    root.attributes('-topmost', True)
    root.config(bg='gray20')
    root.attributes('-transparentcolor', 'gray20')
    #root.overrideredirect(True)

    canvas = tk.Canvas(root, bg='gray20', highlightthickness=0)
    canvas.pack(expand=True, fill='both')

    Da_bg_Image = Image.open("Genshin.png") #换背景
    Da_bg_tk = ImageTk.PhotoImage(Da_bg_Image)
    Da_bg_item = canvas.create_image(0, 0, image=Da_bg_tk, anchor=tk.NW)
    canvas.bg_img = Da_bg_Image
    canvas.bg_tk = Da_bg_tk

    def Realtime_update(event): #自适应边框大小
        new_width, new_height = event.width, event.height
        resized = Da_bg_Image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        new_tk = ImageTk.PhotoImage(resized)
        canvas.itemconfig(Da_bg_item, image=new_tk)
        canvas.bg_img = new_tk

    root.bind("<Configure>", Realtime_update)

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

    def close_window(root):
        print("关闭窗口")
        root.destroy()
    
    keyboard.on_press_key("esc", lambda e: close_window(root))

    root.mainloop()

def main():
    print("Hello from my-rpa!")
    #screenshot = pyautogui.screenshot();
    #screenshot.save("screenshot.png");
    create_overlay()

if __name__ == "__main__":
    main()