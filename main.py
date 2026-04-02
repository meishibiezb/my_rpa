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

def main():
    # screenshot = pyautogui.screenshot();
    # screenshot.save("screenshot.png");
    create_overlay()

if __name__ == "__main__":
    main()
