from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score,classification_report

categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']
twenty_train = fetch_20newsgroups(subset="train", categories=categories, shuffle=True, random_state=42)
vectorizer = TfidfVectorizer()
x_train_tfidf = vectorizer.fit_transform(twenty_train.data)
# print(x_train_tfidf)
y_train = twenty_train.target
x_train, x_test, y_train, y_test = train_test_split(x_train_tfidf, y_train, test_size=0.3, random_state=42)
svm_classifier = SVC(kernel='linear', random_state=42)
svm_classifier.fit(x_train, y_train)
prediction = svm_classifier.predict(x_test)
accuracy = accuracy_score(y_test, prediction)
report = classification_report(y_test,prediction,target_names=twenty_train.target_names)
print("Accuracy = ",accuracy)
print("Classification report =")
print(report)
new_data=[
    "I have a question about computer graphics"
]
x_new=vectorizer.transform(new_data)
newprediction=svm_classifier.predict(x_new)
predicted_category=twenty_train.target_names[newprediction[0]]
print("Predicted category:", predicted_category)