from pydantic import BaseModel


class UserCreate(BaseModel):

    telegram_id: str
    username: str



class SubscriptionCreate(BaseModel):

    user_id: int
    plan: str
    traffic: str
