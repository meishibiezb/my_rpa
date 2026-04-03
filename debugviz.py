import tkinter as tk
import keyboard
import threading
from enum import Enum

class DebugItem(Enum):
    BORDER = 1
    TEXT = 2

class DebugViz:
    def __init__(self):
        self.root = None
        self.canvas = None
        self.is_running = False


        # 画面中的元素
        self.text_id = None

        # 存储物品id
        self.item_ids = []

    def start(self):
        print("start")
        self.is_running = True

        # 设置在另一个线程中运行GUI
        self.thread = threading.Thread(target=self._run_gui, daemon=True)
        self.thread.start()

    def _run_gui(self):
        # 设置窗口基本属性
        self.root = tk.Tk()
        self.root.title = "title"
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        self.root.attributes('-topmost', True)
        self.root.config(bg='gray20')
        self.root.attributes('-transparentcolor', 'gray20')
        self.root.overrideredirect(True)

        # 设置画布
        self.canvas = tk.Canvas(self.root, bg='gray20', highlightthickness=0)
        self.canvas.pack(expand=True, fill='both')
        w = 400
        h = 400
        border_width = 2
        self.canvas.create_rectangle(
            border_width, border_width, 
            w - border_width, h - border_width, 
            outline='red',
            width=2
        )
        self.text_id = self.canvas.create_text(w/2, h/2, text="0", fill='white', font=('Arial', 16))


        keyboard.add_hotkey("shift+esc", lambda: self.close_window())

        print("开启mainloop")
        self.root.mainloop()

    # 设置退出快捷键（以及定义回调函数）
    def close_window(self):
        print("关闭窗口")
        self.is_running = False
        self.root.destroy()

    def update_title(self, text):
        if self.root and self.is_running:
            def change_title(root, text):
                root.title = text
            self.root.after(0, lambda: change_title(text=text))
    
    def update_text(self, text):
        if self.root and self.is_running:
            def change_text(root: DebugViz, text):
                if root and root.text_id:
                    root.canvas.itemconfig(root.text_id, text=text)

            self.root.after(0, lambda: change_text(self, text=text))

    def _create_debug_border(self, x, y, w, h):
        border_width = 2
        border_id = self.canvas.create_rectangle(
            border_width + x, border_width + y, 
            w - border_width + x, h - border_width + y, 
            outline='lime',
            width=2
        )
        item_id = {
            "id" : border_id,
            "type" : DebugItem.BORDER
        }
        self.item_ids.append(item_id)
    
    def create_debug_border(self, x, y, w, h):
        if self.root and self.is_running:
            self.root.after(0, lambda: self._create_debug_border(x, y, w, h))

    def _create_debug_text(self, x, y, t):
        t_id = self.canvas.create_text(x, y, text=t, fill='lime', font=('Arial', 16))
        item_id = {
            "id" : t_id,
            "type" : DebugItem.TEXT
        }
        self.item_ids.append(item_id)

    def create_debug_text(self, x, y, t):
        if self.root and self.is_running:
            self.root.after(0, lambda: self._create_debug_text(x, y, t))

    def delete_debug_item(self, item_id):
        if self.root and self.is_running:
            self.root.after(0, lambda: self.canvas.delete(item_id["id"]))