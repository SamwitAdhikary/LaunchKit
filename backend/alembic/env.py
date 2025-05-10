import os, sys
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# ─── Make sure ‘backend/’ is on Python path ────────────────
HERE = os.path.dirname(__file__)          # …/backend/alembic
BACKEND = os.path.abspath(os.path.join(HERE, os.pardir))  # …/backend
sys.path.insert(0, BACKEND)
# ────────────────────────────────────────────────────────────

import app.models # noqa
from app.models.base import Base      # noqa: your Base
from app.config import settings       # noqa: your DB URL

config = context.config
fileConfig(config.config_file_name)
target_metadata = Base.metadata

def run_migrations_offline():
    url = settings.DATABASE_URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    from sqlalchemy import create_engine
    connectable = create_engine(settings.DATABASE_URL, poolclass=pool.NullPool)
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
