import firebase_admin
from datetime import datetime
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate(r"token.json")

app = firebase_admin.initialize_app(cred)

db = firestore.client()


def insert_book(title, url, text, emotions, hate_speech, author, main_img):
    data = {
        u'title': title,
        u'url': url,
        u'text': text,
        u'emotions': emotions,
        u'hate_speech': hate_speech,
        u'date_uploaded': datetime.utcnow(),
        u'author': author,
        u'main_img': main_img
    }

    db.collection("books").document(title).set(data)


def get_book(title):
    doc_ref = db.collection("books").document(title)

    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        return {}


def get_all_books():
    docs = db.collection("books").stream()   # .where(u'', u'==', True)
    return docs


if __name__ == '__main__':
    # insert_book("test title123", "ww.come", "hello", "ma")
    get_book("test title")
    # get_all_books()
