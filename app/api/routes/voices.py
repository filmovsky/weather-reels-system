from fastapi import APIRouter

router = APIRouter()


@router.get("/voices")
def list_voices():
    return {"voices": []}