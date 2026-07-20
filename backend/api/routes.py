from fastapi import APIRouter


router = APIRouter()


@router.get("/users")
def users():

    return {
        "users": []
    }


@router.get("/subscriptions")
def subscriptions():

    return {
        "subscriptions": []
    }
