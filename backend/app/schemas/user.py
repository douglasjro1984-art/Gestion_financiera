from pydantic import BaseModel, Field

class UserRegister(BaseModel):
    email: str = Field(description="Correo electrónico del usuario")
    username: str = Field(description="Nombre de usuario")
    password: str = Field(description="Contraseña (mínimo 6 caracteres)")

class UserLogin(BaseModel):
    email: str = Field(description="Correo electrónico")
    password: str = Field(description="Contraseña")

class UserResponse(BaseModel):
    id: int
    email: str
    username: str

    class Config:
        from_attributes = True

class TokenResponse(BaseModel):
    access_token: str = Field(description="JWT token")
    token_type: str = "bearer"