from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas.user import UserRegister, UserLogin, UserResponse, TokenResponse
from ..services import auth_service

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    description="Registrar un nuevo usuario"
)
def register(data: UserRegister, db: Session = Depends(get_db)):
    try:
        user = auth_service.register_user(db, data)
        return user
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))

@router.post(
    "/login",
    response_model=TokenResponse,
    description="Iniciar sesión y obtener un JWT token"
)
def login(data: UserLogin, db: Session = Depends(get_db)):
    try:
        token = auth_service.login_user(db, data)
        return TokenResponse(access_token=token)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
