import tkinter as tk
from tkinter import messagebox, font

# Function to calculate percentage and grade
def calculate():
    try:
        total_marks = float(entry_total.get())
        obtained_marks = float(entry_obtained.get())

        if total_marks <= 0:
            raise ValueError("Total marks must be greater than 0")

        percentage = (obtained_marks / total_marks) * 100
        percentage = round(percentage, 4)
        result = f"📊 Percentage: {percentage}%\n"

        if percentage >= 39 and percentage < 45:
            result += "🎓 Grade: D (Pass)"
        elif percentage >= 45 and percentage < 60:
            result += "🎓 Grade: C (Pass)"
        elif percentage >= 60 and percentage < 75:
            result += "🎓 Grade: B (Pass)"
        elif percentage >= 75 and percentage < 85:
            result += "🎓 Grade: A (Pass)"
        elif percentage >= 86 and percentage <= 100:
            result += "🎓 Grade: A+ (Excellent)"
        else:
            result += "❌ You failed."

        messagebox.showinfo("Result", result)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

# Create main window
root = tk.Tk()
root.title("🎯 Percentage Calculator")
root.geometry("400x300")
root.configure(bg="#e8e8e8")

# Smooth round window feel
root.overrideredirect(False)
root.eval('tk::PlaceWindow . center')  # Center window

# Custom font
try:
    gothic_font = font.Font(family="Century Gothic", size=12)
except:
    gothic_font = ("Arial", 12)

# Style helper
def styled_entry(parent):
    box = tk.Entry(parent, font=gothic_font, bg="white", bd=2, relief="flat", highlightthickness=1, highlightbackground="#bbb", highlightcolor="#4CAF50")
    box.pack(pady=8, ipady=5, ipadx=5)
    return box

# Widgets
tk.Label(root, text="Total Marks", bg="#e8e8e8", font=gothic_font).pack(pady=(20, 0))
entry_total = styled_entry(root)

tk.Label(root, text="Obtained Marks", bg="#e8e8e8", font=gothic_font).pack()
entry_obtained = styled_entry(root)

tk.Button(root, text="Calculate", command=calculate,
          font=gothic_font, bg="#4CAF50", fg="white",
          activebackground="#45a049", relief="flat", bd=0,
          padx=20, pady=5).pack(pady=20)

root.mainloop()
