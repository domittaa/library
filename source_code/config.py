from pydantic_settings import BaseSettings


class Settings(BaseSettings):  # determine values that aren't passed as keyword arguments by reading from environment
    database_url: str
    test_database_url: str
    echo_sql: bool = True
    test: bool = False
    project_name: str = "Library"
    debug_logs: bool = False


settings = Settings()
