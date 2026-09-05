import tkinter as tk
import pickle
import re


with open("log_model.pkl", "rb") as file:
    log_model = pickle.load(file)

with open("nb_model.pkl", "rb") as file:
    nb_model = pickle.load(file)

with open("svm_model.pkl", "rb") as file:
    svm_model = pickle.load(file)

with open("vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)


def clean_tweet(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"[^a-z\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    text = text.strip()

    return text


BORDER_COLOR = "#3a5a48"
BACKGROUND = "#0d1f17"
CARD_BACKGROUND = "#1a2e24"

WHITE = "#ffffff"
GREY = "#888888"

POSITIVE_COLOR = "#4caf50"
NEGATIVE_COLOR = "#e05252"

ACTIVE_COLOR = "#1a3a2a"


window = tk.Tk()

window.title("Sentiment Analysis")
window.geometry("700x550")
window.configure(bg=BACKGROUND)

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)


outer_frame = tk.Frame(
    window,
    bg=BACKGROUND,
    highlightbackground=BORDER_COLOR,
    highlightthickness=2
)

outer_frame.grid(
    row=0,
    column=0,
    sticky="nsew",
    padx=8,
    pady=8
)

outer_frame.rowconfigure(0, weight=1)
outer_frame.columnconfigure(1, weight=1)


sidebar = tk.Frame(
    outer_frame,
    bg=BACKGROUND,
    width=160
)

sidebar.grid(
    row=0,
    column=0,
    sticky="ns"
)

sidebar.grid_propagate(False)
sidebar.columnconfigure(0, weight=1)


main_area = tk.Frame(
    outer_frame,
    bg=BACKGROUND
)

main_area.grid(
    row=0,
    column=1,
    sticky="nsew"
)

main_area.rowconfigure(0, weight=1)
main_area.columnconfigure(0, weight=1)


analyze_page = tk.Frame(
    main_area,
    bg=BACKGROUND
)

accuracy_page = tk.Frame(
    main_area,
    bg=BACKGROUND
)

about_page = tk.Frame(
    main_area,
    bg=BACKGROUND
)


def show_analyze():

    accuracy_page.grid_remove()
    about_page.grid_remove()

    analyze_page.grid(
        row=0,
        column=0,
        sticky="nsew"
    )

    analyze_button.config(
        bg=ACTIVE_COLOR
    )

    accuracy_button.config(
        bg=BACKGROUND
    )

    about_button.config(
        bg=BACKGROUND
    )


def show_accuracy():

    analyze_page.grid_remove()
    about_page.grid_remove()

    accuracy_page.grid(
        row=0,
        column=0,
        sticky="nsew"
    )

    analyze_button.config(
        bg=BACKGROUND
    )

    accuracy_button.config(
        bg=ACTIVE_COLOR
    )

    about_button.config(
        bg=BACKGROUND
    )


def show_about():

    analyze_page.grid_remove()
    accuracy_page.grid_remove()

    about_page.grid(
        row=0,
        column=0,
        sticky="nsew"
    )

    analyze_button.config(
        bg=BACKGROUND
    )

    accuracy_button.config(
        bg=BACKGROUND
    )

    about_button.config(
        bg=ACTIVE_COLOR
    )


analyze_button = tk.Label(
    sidebar,
    text="Analyze",
    font=("Courier", 11, "bold"),
    bg=ACTIVE_COLOR,
    fg=WHITE,
    padx=15,
    pady=8,
    cursor="hand2"
)

analyze_button.grid(
    row=0,
    column=0,
    padx=15,
    pady=(15, 8),
    sticky="ew"
)

analyze_button.bind(
    "<Button-1>",
    lambda event: show_analyze()
)


accuracy_button = tk.Label(
    sidebar,
    text="Accuracy",
    font=("Courier", 11, "bold"),
    bg=BACKGROUND,
    fg=WHITE,
    padx=15,
    pady=8,
    cursor="hand2"
)

accuracy_button.grid(
    row=1,
    column=0,
    padx=15,
    pady=8,
    sticky="ew"
)

accuracy_button.bind(
    "<Button-1>",
    lambda event: show_accuracy()
)


about_button = tk.Label(
    sidebar,
    text="About",
    font=("Courier", 11, "bold"),
    bg=BACKGROUND,
    fg=WHITE,
    padx=15,
    pady=8,
    cursor="hand2"
)

about_button.grid(
    row=2,
    column=0,
    padx=15,
    pady=8,
    sticky="ew"
)

about_button.bind(
    "<Button-1>",
    lambda event: show_about()
)


analyze_page.rowconfigure(3, weight=1)
analyze_page.columnconfigure(0, weight=1)


analyze_title = tk.Label(
    analyze_page,
    text="SENTIMENT ANALYSIS",
    font=("Courier", 15, "bold"),
    bg=BACKGROUND,
    fg=WHITE
)

analyze_title.grid(
    row=0,
    column=0,
    pady=15
)


tweet_section = tk.Frame(
    analyze_page,
    bg=BACKGROUND,
    highlightbackground=BORDER_COLOR,
    highlightthickness=1
)

tweet_section.grid(
    row=1,
    column=0,
    padx=20,
    pady=8,
    sticky="ew"
)

tweet_section.columnconfigure(0, weight=1)


tweet_label = tk.Label(
    tweet_section,
    text="TWEET",
    font=("Courier", 11, "bold"),
    bg=BACKGROUND,
    fg=WHITE
)

tweet_label.grid(
    row=0,
    column=0,
    sticky="w",
    padx=12,
    pady=(8, 0)
)


PLACEHOLDER_TEXT = "Type your text here..."


tweet_input = tk.Text(
    tweet_section,
    height=4,
    width=55,
    font=("Courier", 10),
    bg=CARD_BACKGROUND,
    fg=GREY,
    insertbackground=WHITE,
    relief="flat",
    padx=8,
    pady=8
)

tweet_input.grid(
    row=1,
    column=0,
    padx=12,
    pady=8,
    sticky="ew"
)


char_count_label = tk.Label(
    tweet_section,
    text="0/280",
    font=("Courier", 9),
    bg=BACKGROUND,
    fg=GREY
)

char_count_label.grid(
    row=2,
    column=0,
    sticky="e",
    padx=12,
    pady=(0, 5)
)


def clear_placeholder(event):

    current_text = tweet_input.get(
        "1.0",
        "end-1c"
    )

    if current_text == PLACEHOLDER_TEXT:

        tweet_input.delete(
            "1.0",
            "end"
        )

        tweet_input.config(
            fg=WHITE
        )


def add_placeholder(event):

    current_text = tweet_input.get(
        "1.0",
        "end-1c"
    )

    if current_text == "":

        tweet_input.insert(
            "1.0",
            PLACEHOLDER_TEXT
        )

        tweet_input.config(
            fg=GREY
        )


tweet_input.insert(
    "1.0",
    PLACEHOLDER_TEXT
)

tweet_input.bind(
    "<FocusIn>",
    clear_placeholder
)

tweet_input.bind(
    "<FocusOut>",
    add_placeholder
)


def update_char_count(event):

    text = tweet_input.get(
        "1.0",
        "end-1c"
    )

    if text == PLACEHOLDER_TEXT:
        count = 0
    else:
        count = len(text)

    char_count_label.config(
        text=str(count) + "/280"
    )


tweet_input.bind(
    "<KeyRelease>",
    update_char_count
)


predictions_frame = tk.Frame(
    analyze_page,
    bg=BACKGROUND,
    highlightbackground=BORDER_COLOR,
    highlightthickness=1
)

predictions_frame.grid(
    row=3,
    column=0,
    padx=20,
    pady=12,
    sticky="ew"
)

predictions_frame.columnconfigure(0, weight=1)
predictions_frame.columnconfigure(1, weight=1)
predictions_frame.columnconfigure(2, weight=1)


predictions_title = tk.Label(
    predictions_frame,
    text="MODEL PREDICTIONS",
    font=("Courier", 11, "bold"),
    bg=BACKGROUND,
    fg=WHITE
)

predictions_title.grid(
    row=0,
    column=0,
    columnspan=3,
    sticky="w",
    padx=12,
    pady=(8, 10)
)


log_name_label = tk.Label(
    predictions_frame,
    text="Log. Regression",
    font=("Courier", 9),
    bg=BACKGROUND,
    fg=WHITE
)

log_name_label.grid(
    row=1,
    column=0,
    padx=8,
    pady=3
)


nb_name_label = tk.Label(
    predictions_frame,
    text="Naive Bayes",
    font=("Courier", 9),
    bg=BACKGROUND,
    fg=WHITE
)

nb_name_label.grid(
    row=1,
    column=1,
    padx=8,
    pady=3
)


svm_name_label = tk.Label(
    predictions_frame,
    text="Linear SVM",
    font=("Courier", 9),
    bg=BACKGROUND,
    fg=WHITE
)

svm_name_label.grid(
    row=1,
    column=2,
    padx=8,
    pady=3
)


log_result_label = tk.Label(
    predictions_frame,
    text="-",
    font=("Courier", 10, "bold"),
    bg=CARD_BACKGROUND,
    fg=WHITE,
    padx=10,
    pady=6
)

log_result_label.grid(
    row=2,
    column=0,
    padx=8,
    pady=(0, 12)
)


nb_result_label = tk.Label(
    predictions_frame,
    text="-",
    font=("Courier", 10, "bold"),
    bg=CARD_BACKGROUND,
    fg=WHITE,
    padx=10,
    pady=6
)

nb_result_label.grid(
    row=2,
    column=1,
    padx=8,
    pady=(0, 12)
)


svm_result_label = tk.Label(
    predictions_frame,
    text="-",
    font=("Courier", 10, "bold"),
    bg=CARD_BACKGROUND,
    fg=WHITE,
    padx=10,
    pady=6
)

svm_result_label.grid(
    row=2,
    column=2,
    padx=8,
    pady=(0, 12)
)


final_verdict_label = tk.Label(
    predictions_frame,
    text="Final Verdict: -",
    font=("Courier", 12, "bold"),
    bg=BACKGROUND,
    fg=WHITE
)

final_verdict_label.grid(
    row=3,
    column=0,
    columnspan=3,
    pady=(0, 12)
)


analyze_action_button = tk.Label(
    analyze_page,
    text="ANALYZE",
    font=("Courier", 10, "bold"),
    bg=ACTIVE_COLOR,
    fg=WHITE,
    padx=20,
    pady=6,
    cursor="hand2"
)

analyze_action_button.grid(
    row=2,
    column=0,
    pady=10
)


def run_prediction(event=None):

    tweet = tweet_input.get(
        "1.0",
        "end-1c"
    )

    if tweet == PLACEHOLDER_TEXT:
        return

    if tweet.strip() == "":
        return

    cleaned_tweet = clean_tweet(tweet)

    vectorized_tweet = vectorizer.transform(
        [cleaned_tweet]
    )

    log_prediction = log_model.predict(
        vectorized_tweet
    )[0]

    nb_prediction = nb_model.predict(
        vectorized_tweet
    )[0]

    svm_prediction = svm_model.predict(
        vectorized_tweet
    )[0]

    if log_prediction == 1:
        log_text = "Positive"
        log_color = POSITIVE_COLOR
    else:
        log_text = "Negative"
        log_color = NEGATIVE_COLOR

    if nb_prediction == 1:
        nb_text = "Positive"
        nb_color = POSITIVE_COLOR
    else:
        nb_text = "Negative"
        nb_color = NEGATIVE_COLOR

    if svm_prediction == 1:
        svm_text = "Positive"
        svm_color = POSITIVE_COLOR
    else:
        svm_text = "Negative"
        svm_color = NEGATIVE_COLOR

    log_result_label.config(
        text=log_text,
        fg=log_color
    )

    nb_result_label.config(
        text=nb_text,
        fg=nb_color
    )

    svm_result_label.config(
        text=svm_text,
        fg=svm_color
    )

    votes = [
        log_prediction,
        nb_prediction,
        svm_prediction
    ]

    average = sum(votes) / len(votes)

    if average >= 0.5:
        final_sentiment = "Positive"
        final_color = POSITIVE_COLOR
    else:
        final_sentiment = "Negative"
        final_color = NEGATIVE_COLOR

    final_verdict_label.config(
        text="Final Verdict: {} ({:.2f})".format(
            final_sentiment,
            average
        ),
        fg=final_color
    )

    tweet_input.delete(
        "1.0",
        "end"
    )

    tweet_input.insert(
        "1.0",
        PLACEHOLDER_TEXT
    )

    tweet_input.config(
        fg=GREY
    )

    char_count_label.config(
        text="0/280"
    )


analyze_action_button.bind(
    "<Button-1>",
    run_prediction
)


accuracy_page.columnconfigure(0, weight=1)


accuracy_title = tk.Label(
    accuracy_page,
    text="MODEL ACCURACY",
    font=("Courier", 15, "bold"),
    bg=BACKGROUND,
    fg=WHITE
)

accuracy_title.grid(
    row=0,
    column=0,
    pady=15
)


accuracy_cards_frame = tk.Frame(
    accuracy_page,
    bg=BACKGROUND
)

accuracy_cards_frame.grid(
    row=1,
    column=0,
    padx=20,
    pady=15
)


log_card = tk.Label(
    accuracy_cards_frame,
    text="Log. Regression\n\n78.2%",
    font=("Courier", 10, "bold"),
    bg=CARD_BACKGROUND,
    fg=WHITE,
    padx=18,
    pady=15,
    justify="center",
    highlightbackground=BORDER_COLOR,
    highlightthickness=1
)

log_card.grid(
    row=0,
    column=0,
    padx=6
)


nb_card = tk.Label(
    accuracy_cards_frame,
    text="Naive Bayes\n\n76.2%",
    font=("Courier", 10, "bold"),
    bg=CARD_BACKGROUND,
    fg=WHITE,
    padx=18,
    pady=15,
    justify="center",
    highlightbackground=BORDER_COLOR,
    highlightthickness=1
)

nb_card.grid(
    row=0,
    column=1,
    padx=6
)


svm_card = tk.Label(
    accuracy_cards_frame,
    text="Linear SVM\n\n77.9%",
    font=("Courier", 10, "bold"),
    bg=CARD_BACKGROUND,
    fg=WHITE,
    padx=18,
    pady=15,
    justify="center",
    highlightbackground=BORDER_COLOR,
    highlightthickness=1
)

svm_card.grid(
    row=0,
    column=2,
    padx=6
)


about_page.columnconfigure(0, weight=1)
about_page.rowconfigure(1, weight=1)


about_title = tk.Label(
    about_page,
    text="ABOUT",
    font=("Courier", 15, "bold"),
    bg=BACKGROUND,
    fg=WHITE
)

about_title.grid(
    row=0,
    column=0,
    pady=15
)


about_section = tk.Frame(
    about_page,
    bg=BACKGROUND,
    highlightbackground=BORDER_COLOR,
    highlightthickness=1
)

about_section.grid(
    row=1,
    column=0,
    padx=20,
    pady=8,
    sticky="nsew"
)


about_text = tk.Label(
    about_section,
    text=(
        "This is a simple sentiment analysis tool built using machine learning "
        "to understand whether a tweet is positive or negative. It uses "
        "Logistic Regression, Naive Bayes, and Linear SVM to make predictions "
        "and compare their results. The tweet is first cleaned and converted "
        "into numerical features before being passed to the trained models. "
        "This project was built as a way to learn and explore machine learning.\n\n"
        "-GP"
    ),
    font=("Courier", 9),
    bg=BACKGROUND,
    fg="#cccccc",
    justify="left",
    wraplength=500
)

about_text.grid(
    row=0,
    column=0,
    sticky="nw",
    padx=20,
    pady=20
)


show_analyze()

window.mainloop()