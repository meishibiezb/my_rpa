import tkinter as tk
import keyboard
import threading

class DebugViz:
    def __init__(self):
        self.root = None
        self.canvas = None
        self.is_running = False

        # 画面中的元素
        self.text_id = None

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
            outline='lime',
            width=2
        )
        self.text_id = self.canvas.create_text(w/2, h/2, text="0", fill='white', font=('Arial', 16))

        # 设置退出快捷键（以及定义回调函数）
        def close_window(root):
            print("关闭窗口")
            self.is_running = False
            root.destroy()
        keyboard.on_press_key("esc", lambda e: close_window(self.root))

        print("开启mainloop")
        self.root.mainloop()

    def update_title(self, text):
        if self.root:
            def change_title(root, text):
                root.title = text
            self.root.after(0, lambda: change_title(text=text))
    
    def update_text(self, text):
        if self.root:
            def change_text(root: DebugViz, text):
                if root and root.text_id:
                    root.canvas.itemconfig(root.text_id, text=text)

            self.root.after(0, lambda: change_text(self, text=text))