from fastapi import APIRouter

from app.models import FakeNewsInput
from app.utils import predict_fake_news

fake_news_predict_router = APIRouter(prefix="/api/v1")

@fake_news_predict_router.post("/fake-news/predict")
def fake_news_prediction(fake_news_input: FakeNewsInput):
    # 1 is Real, 0 is Fake
    return "false" if (predict_fake_news(fake_news_input.fake_news) == 1) else "true"