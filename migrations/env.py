import os
from logging.config import fileConfig
from alembic import context
from dotenv import load_dotenv
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from models.users import Base

config = context.config
fileConfig(config.config_file_name)

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

section = config.config_ini_section
config.set_section_option(section, "DB_USER", os.getenv('DB_USER'))
config.set_section_option(section, "DB_PASSWORD", os.getenv('DB_PASSWORD'))
config.set_section_option(section, "DB_HOST", os.getenv('DB_HOST'))
config.set_section_option(section, "DB_PORT", os.getenv('DB_PORT'))
config.set_section_option(section, "DB_NAME", os.getenv('DB_NAME'))
target_metadata = Base.metadata



def run_migrations_offline() -> None:

    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:

    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
