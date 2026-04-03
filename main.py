import debugviz
import time
import pyautogui

def create_overlay():
    dbgv = debugviz.DebugViz()
    dbgv.start()

    count = 0;

    while dbgv.is_running:
        dbgv.update_text(f"{count}")
        time.sleep(0.001)
        count += 1

        current_position = pyautogui.position()
        dbgv.create_debug_border(current_position.x, current_position.y, 4, 4)

def main():
    create_overlay()

if __name__ == "__main__":
    main()
