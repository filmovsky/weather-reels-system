from fastapi import APIRouter

router = APIRouter()


@router.get("/layouts")
def list_layouts():
    return {"layouts": []}