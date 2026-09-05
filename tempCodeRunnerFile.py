import tkinter as tk

window = tk.Tk()
window.title("Sentiment Analysis")
window.geometry("900x650")
window.configure(bg="#0d1f17")

sidebar = tk.Frame(window, bg="#0d1f17", width=200)
sidebar.pack(side="left", fill="y")

main_area = tk.Frame(window, bg="#0d1f17")
main_area.pack(side="left", fill="both", expand=True)

analyze_page = tk.Frame(main_area, bg="#0d1f17")
accuracy_page = tk.Frame(main_area, bg="#0d1f17")

analyze_title = tk.Label(
    analyze_page, text="SENTIMENT ANALYSIS",
    font=("Courier", 18, "bold"), bg="#0d1f17", fg="white"
)
analyze_title.pack(pady=20)

tweet_label = tk.Label(
    analyze_page, text="TWEET", font=("Courier", 12, "bold"),
    bg="#0d1f17", fg="white"
)
tweet_label.pack(anchor="w", padx=30, pady=(10, 0))

tweet_input = tk.Text(
    analyze_page, height=4, width=70, font=("Courier", 11),
    bg="#1a2e24", fg="white", insertbackground="white",
    relief="flat", padx=10, pady=10
)
tweet_input.pack(padx=30, pady=10)

char_count_label = tk.Label(
    analyze_page, text="0/280", font=("Courier", 10),
    bg="#0d1f17", fg="#888888"
)
char_count_label.pack(anchor="e", padx=30)


def update_char_count(event):
    text = tweet_input.get("1.0", "end-1c")
    count = len(text)
    char_count_label.config(text=f"{count}/280")


tweet_input.bind("<KeyRelease>", update_char_count)

analyze_action_button = tk.Label(
    analyze_page, text="ANALYZE", font=("Courier", 11, "bold"),
    bg="#1a3a2a", fg="white", padx=20, pady=8, cursor="hand2"
)
analyze_action_button.pack(pady=15)


def show_analyze(event):
    accuracy_page.pack_forget()
    analyze_page.pack(fill="both", expand=True)
    analyze_button.config(bg="#1a3a2a")
    accuracy_button.config(bg="#0d1f17")


def show_accuracy(event):
    analyze_page.pack_forget()
    accuracy_page.pack(fill="both", expand=True)
    accuracy_button.config(bg="#1a3a2a")
    analyze_button.config(bg="#0d1f17")


analyze_button = tk.Label(
    sidebar, text="Analyze", font=("Courier", 12, "bold"),
    bg="#1a3a2a", fg="white", padx=20, pady=10, cursor="hand2"
)
analyze_button.pack(pady=(20, 10), padx=20, fill="x")
analyze_button.bind("<Button-1>", show_analyze)

accuracy_button = tk.Label(
    sidebar, text="Accuracy", font=("Courier", 12, "bold"),
    bg="#0d1f17", fg="white", padx=20, pady=10, cursor="hand2"
)
accuracy_button.pack(pady=10, padx=20, fill="x")
accuracy_button.bind("<Button-1>", show_accuracy)

analyze_page.pack(fill="both", expand=True)

window.mainloop()