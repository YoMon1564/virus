import time
import tkinter as tk
import threading
import random

def create_info_window():
    """创建一个简单的信息提示窗口"""
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # 随机生成窗口在屏幕内的坐标位置（这里可以调整范围让展示更合理）
    a = random.randint(0, width - 200)  # 限制窗口不要超出屏幕边界
    b = random.randint(0, height - 150)
    window.title('Error')
    window.geometry(f"300x150+{a}+{b}")
    tk.Label(window,
             text='Error',  # 可以修改为你想展示的具体内容
             font=('楷体', 12),
             width=15, height=10
             ).pack()
    window.after(100, window.destroy)  #自动销毁该窗口
    window.mainloop()


def start_windows():
    """启动多个提示窗口的函数，这里可以控制数量等情况"""
    num_windows = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999  # 可以修改这个值来控制要弹出窗口的大致数量，比如改成循环持续生成可模拟无限数量但要注意合理控制
    threads = []
    for _ in range(num_windows):
        t = threading.Thread(target=create_info_window)
        threads.append(t)
        t.start()
        time.sleep(0)  # 可以调整间隔时间，控制窗口弹出的频率


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Error")
    root.geometry("300x200")
    start_btn = tk.Button(root, text="点一下", command=start_windows)
    start_btn.pack(pady=80)
    root.mainloop()