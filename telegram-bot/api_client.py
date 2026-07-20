import httpx

from config import BACKEND_URL


async def get_users():

    async with httpx.AsyncClient() as client:

        response = await client.get(
            f"{BACKEND_URL}/api/users"
        )

        return response.json()
