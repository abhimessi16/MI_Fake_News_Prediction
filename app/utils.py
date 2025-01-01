import app.main as session

def predict_fake_news(fake_news: str):
    fake_news_vec = session.vectorization.transform([fake_news])
    return session.model.predict(fake_news_vec)