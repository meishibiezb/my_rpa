import debugviz
import time
import pyautogui
import threading

def create_overlay():
    dbgv = debugviz.DebugViz()
    dbgv.start()

    count = 0;

    while dbgv.is_running:
        dbgv.update_text(f"{count}")
        time.sleep(0.01)
        count += 1

        def callback(self: debugviz.DebugViz, item_id):
            timer = threading.Timer(5.0, lambda: self.canvas.delete(item_id["id"]))
            timer.start()

        current_position = pyautogui.position()
        dbgv.create_debug_border(current_position.x, current_position.y, 4, 4, callback)

def main():
    create_overlay()

if __name__ == "__main__":
    main()
