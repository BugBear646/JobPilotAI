from fastapi import APIRouter

router = APIRouter(
    prefix="/api",
    tags=["API"],
)


@router.get("/")
def api_root():
    return {
        "success": True,
        "message": "JobPilotAI API Running"
    }


@router.get("/ping")
def ping():
    return {
        "status": "ok"
    }


@router.get("/version")
def version():
    return {
        "version": "0.1.0"
    }