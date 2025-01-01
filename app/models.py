from pydantic import BaseModel

class FakeNewsInput(BaseModel):
    fake_news: str