from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime
)

from database import Base
from datetime import datetime


class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    telegram_id = Column(
        String,
        unique=True
    )

    username = Column(
        String
    )

    is_admin = Column(
        Boolean,
        default=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )



class Subscription(Base):

    __tablename__ = "subscriptions"

    id = Column(
        Integer,
        primary_key=True
    )

    user_id = Column(
        Integer
    )

    plan = Column(
        String
    )

    traffic = Column(
        String
    )

    expire_date = Column(
        DateTime
    )



class Server(Base):

    __tablename__ = "servers"

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(
        String
    )

    country = Column(
        String
    )

    address = Column(
        String
    )


class Panel(Base):

    __tablename__ = "panels"

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(
        String
    )

    api_url = Column(
        String
    )

    token = Column(
        String
    )
