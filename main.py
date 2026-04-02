import debugviz
import time

def create_overlay():
    dbgv = debugviz.DebugViz()
    dbgv.start()

    count = 0;

    while dbgv.is_running:
        dbgv.update_text(f"{count}")
        # print(f"{count}")
        time.sleep(0.1)
        count += 1
    # root = tk.Tk()
    # root.title = "111"

    # screen_width = root.winfo_screenwidth()
    # screen_height = root.winfo_screenheight()
    # root.geometry(f"{screen_width}x{screen_height}+0+0")
    
    # root.attributes('-topmost', True)
    # root.config(bg='gray20')
    # root.attributes('-transparentcolor', 'gray20')
    # root.overrideredirect(True)

    # canvas = tk.Canvas(root, bg='gray20', highlightthickness=0)
    # canvas.pack(expand=True, fill='both')

    # w = 400
    # h = 400
    # border_width = 2
    # canvas.create_rectangle(
    #     border_width, border_width, 
    #     w - border_width, h - border_width, 
    #     outline='lime',
    #     width=2
    # )

    # canvas.create_text(w/2, h/2, text="Canvas 画出的边框", fill='white', font=('Arial', 16))

    # def close_window(root):
    #     print("关闭窗口")
    #     root.destroy()
    
    # keyboard.on_press_key("esc", lambda e: close_window(root))

    # root.mainloop()

def main():
    # screenshot = pyautogui.screenshot();
    # screenshot.save("screenshot.png");
    create_overlay()

if __name__ == "__main__":
    main()
