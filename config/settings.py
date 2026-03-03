import logging
import sys
from pydantic_settings import BaseSettings, SettingsConfigDict


# ====== Logging Setup ======
def setup_logging() -> logging.Logger:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.StreamHandler(sys.stdout)],
    )
    return logging.getLogger("travel-agent")


logger = setup_logging()


# ====== Pydantic Settings / Env Validation ======
class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    openai_api_key: str
    app_port: int = 7777
    llm_model: str = "gpt-4o-mini"
    data_folder: str = "data"


try:
    settings = Settings()
    logger.info("Configuration loaded successfully.")
except Exception as e:
    logger.critical(f"Missing required environment variables: {e}")
    sys.exit(1)


# ====== Convenience exports (backwards-compatible) ======
llm_model = settings.llm_model
api_key = settings.openai_api_key
app_port = settings.app_port
data_folder = settings.data_folder
