import time
import tkinter as tk
import threading
import random

def create_info_window():
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randint(0, width - 200)
    b = random.randint(0, height - 150)
    window.title('Error')
    window.geometry(f"300x150+{a}+{b}")
    tk.Label(window, text='Error', font=('楷体', 12), width=15, height=10).pack()
    window.after(100,window.destroy)
    window.mainloop()

def start_windows():
    num_windows = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    threads = []
    for _ in range(num_windows):
        t = threading.Thread(target=create_info_window)
        threads.append(t)
        t.start()
        time.sleep(0)

if __name__ == "__main__":
    root = tk.Tk ()
    root.title("Error")
    root.geometry("300x200")
    start_btn = tk.Button(root, text="点一下", command=start_windows)
    start_btn.pack(pady=80)
    root.mainloop()