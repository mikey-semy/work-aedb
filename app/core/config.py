from typing import Dict, List, Any
from pydantic import Field, SecretStr
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)

from app.const import env_path

class Settings(BaseSettings):
    
    token_key: SecretStr

    aws_service_name: str = 's3'
    aws_region: str
    aws_endpoint: str
    aws_bucket_name: str
    aws_access_key_id: str
    aws_secret_access_key: str
    
    dsn: str =  Field(default="sqlite+aiosqlite:///./database_aedb.db")
    docs_access: bool = True

    allow_origins: List[str] = Field(default_factory=list)
    allow_credentials: bool = True
    allow_methods: List[str] = ["*"]
    allow_headers: List[str] = ["*"]

    @property
    def cors_params(self) -> Dict[str, Any]:
        return {
            "allow_origins": self.allow_origins,
            "allow_credentials": self.allow_credentials,
            "allow_methods": self.allow_methods,
            "allow_headers": self.allow_headers,
        }
        
    
    
    
    model_config = SettingsConfigDict(
        env_file=env_path,
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        extra='allow'
    )

config = Settings()
cors_params = config.cors_params
