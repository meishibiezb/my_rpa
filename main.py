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

    root.mainloop()

def main():
    print("Hello from my-rpa!")
    screenshot = pyautogui.screenshot();
    screenshot.save("screenshot.png");
    create_overlay()

if __name__ == "__main__":
    main()
