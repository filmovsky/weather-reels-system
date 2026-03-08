from fastapi import APIRouter

router = APIRouter()


@router.get("/regions")
def list_regions():
    return {"regions": []}