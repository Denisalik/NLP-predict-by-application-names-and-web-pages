import json

from tabNamesCat import load_model, sentence_clean, get_mappings_to_category

from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from model import SessionLocal, Activity, activity_to_dict

app = FastAPI(title='app')
vector_clf, clf = load_model()
mappings = get_mappings_to_category()

def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/download')
def download(session: Session = Depends(get_session)):
    try:
        items = [activity_to_dict(item) for item in session.query(Activity).all()]
        with open('/ML/data.json', 'w') as f:
            json.dump(items, f, ensure_ascii=False)
        return True
    except:
        return False

class Tabs(BaseModel):
    names: list[str]
    # names = ["Купить Картридж лазерный Cactus CS-CE285AS (CE285A), черный, 1600 страниц, совместимый, для LJP M1132 / M1212nf / M1217nfw / P1102 / P1102w / P1214nfh / M1132s в Омске. Цены от интернет-магазина e2e4 - Google Chrome"]
    # returns ["Utilities"]
@app.post('/predict/')
def predict(tabs: Tabs):
    sentences = [sentence_clean(sentence) for sentence in tabs.names]
    vectors = vector_clf.transform(sentences)
    categories = clf.predict(vectors)
    return [mappings[category] for category in categories]
