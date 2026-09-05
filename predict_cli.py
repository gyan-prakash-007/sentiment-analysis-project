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
    text = re.sub(r"\s+", " ", text).strip()
    return text


tweet = input("Enter a tweet: ")

cleaned = clean_tweet(tweet)
vectorized = vectorizer.transform([cleaned])

log_pred = log_model.predict(vectorized)[0]
nb_pred = nb_model.predict(vectorized)[0]
svm_pred = svm_model.predict(vectorized)[0]

if log_pred == 1:
    print("Logistic regression: ", "positive")
else:
    print("Logistic regression: ", "negative")


if nb_pred == 1:
    print("Naive bayes: ", "positive")
else:
    print("Naive bayes: ", "negative")


if svm_pred == 1:
    print("SVM: ", "positive")
else:
    print("SVM :", "negative")


votes = [log_pred, nb_pred, svm_pred]
average = sum(votes) / len(votes)

final = "Positive" if average >= 0.5 else "Negative"
print("Final Verdict:", final, f"({average:.2f} average score)")