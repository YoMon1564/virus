import tkinter as tk
from tkinter import messagebox

print("<DigitalTrailBlazer>")


def disable_close(event):
    try:
        messagebox.showinfo("提示", "此窗口无法通过常规方式关闭哦！")
        return "break"
    except tk.TclError:
        # 捕获可能出现的Tcl相关错误，比如窗口已经处于关闭等异常状态时
        pass


try:
    root = tk.Tk()
    # 设置窗口标题
    root.title("关不掉的窗口")
    # 设置窗口大小
    root.geometry("300x200")
    # 绑定关闭窗口事件，阻止其正常关闭
    root.protocol("WM_DELETE_WINDOW", disable_close)

    # 添加一个简单的标签说明情况
    label = tk.Label(root, text="小鬼火热了吧?")
    label.pack(pady=50)

    root.mainloop()
except tk.TclError as e:
    # 捕获主窗口初始化及运行过程中可能出现的Tcl错误并打印提示信息
    print(f"出现Tcl相关错误: {e}")
except Exception as e:
    # 捕获其他可能出现的未知异常并打印提示信息
    print(f"出现未知异常: {e}")