from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    echo_sql: bool = True
    test: bool = False
    project_name: str = "Projekt Biblioteka"
    debug_logs: bool = False


settings = Settings()
