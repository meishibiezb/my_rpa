import debugviz
import time
import pyautogui
import threading

def create_overlay():
    dbgv = debugviz.DebugViz()
    dbgv.start()

    count = 0;

    def o():
        # 定位目标图像
        def delete_border(self: debugviz.DebugViz, item_id):
            timer = threading.Timer(0.3, lambda: self.delete_debug_item(item_id))
            timer.start()
        location = None
        while dbgv.is_running:
            # time.sleep(1)
            try:
                location = pyautogui.locateOnScreen('target.png', grayscale=True, confidence=0.8)
            except pyautogui.ImageNotFoundException:
                pass
            if location:
                # print("Found Image")
                dbgv.create_debug_border(location.left, location.top, location.width, location.height, delete_border)

    o_thread = threading.Thread(target=o, daemon=True)
    o_thread.start()

    while dbgv.is_running:
        dbgv.update_text(f"{count}")
        time.sleep(0.001)
        count += 1
        dbgv.lift()

        # def callback(self: debugviz.DebugViz, item_id):
        #     timer = threading.Timer(1.0, lambda: self.delete_debug_item(item_id))
        #     timer.start()

        # current_position = pyautogui.position()
        # # 输出鼠标轨迹（矩形）
        # dbgv.create_debug_border(current_position.x, current_position.y, 4, 4, callback)
        # # 输出鼠标轨迹（文字）
        # if count % 107 == 0:
        #     dbgv.create_debug_text(current_position.x, current_position.y, "olo", callback)



def main():
    create_overlay()

if __name__ == "__main__":
    main()
