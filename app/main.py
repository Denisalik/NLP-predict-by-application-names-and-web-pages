import json

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from model import SessionLocal, Activity, activity_to_dict

app = FastAPI(title='app')


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


@app.get('/predict/{tab_name}')
def predict(tab_name: str):
    return tab_name
