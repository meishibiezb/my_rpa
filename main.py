import pyautogui
import tkinter as tk

def create_overlay():
    root = tk.Tk()
    root.title = "111"
    root.geometry("400x400+100+100")
    root.attributes('-topmost', True)
    root.config(bg='gray20')
    root.attributes('-transparentcolor', 'gray20')
    # root.overrideredirect(True)

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

    root.mainloop()

def main():
    print("Hello from my-rpa!")
    screenshot = pyautogui.screenshot();
    screenshot.save("screenshot.png");
    create_overlay()

if __name__ == "__main__":
    main()
