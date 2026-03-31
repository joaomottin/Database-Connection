from __future__ import annotations

"""Template generico para conexao com banco de dados.

Uso rapido:
1) Instale dependencia base: pip install sqlalchemy
2) Defina a variavel de ambiente DATABASE_URL
3) Execute este arquivo para testar a conexao

Exemplos de DATABASE_URL:
- SQLite: sqlite:///./app.db
- PostgreSQL: postgresql+psycopg://usuario:senha@localhost:5432/meu_banco
- MySQL: mysql+pymysql://usuario:senha@localhost:3306/meu_banco
- SQL Server: mssql+pyodbc://usuario:senha@servidor:1433/meu_banco?driver=ODBC+Driver+18+for+SQL+Server&Encrypt=yes&TrustServerCertificate=yes
"""

import os
from typing import Any

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError


def get_database_url() -> str:
    database_url = os.getenv("DATABASE_URL", "").strip()
    if not database_url:
        raise RuntimeError(
            "Defina a variavel de ambiente DATABASE_URL antes de executar."
        )
    return database_url


def create_db_engine(database_url: str | None = None, *, echo: bool = False) -> Engine:
    url = database_url or get_database_url()
    return create_engine(url, pool_pre_ping=True, future=True, echo=echo)


def test_connection(engine: Engine) -> None:
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))


def fetch_all(
    engine: Engine,
    query: str,
    params: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    with engine.connect() as connection:
        result = connection.execute(text(query), params or {})
        return [dict(row._mapping) for row in result]


def execute_non_query(
    engine: Engine,
    query: str,
    params: dict[str, Any] | None = None,
) -> int:
    with engine.begin() as connection:
        result = connection.execute(text(query), params or {})
        return int(result.rowcount or 0)


def main() -> int:
    try:
        engine = create_db_engine()
        test_connection(engine)
        print("Conexao OK")

        # Exemplo de consulta simples para validar retorno.
        rows = fetch_all(engine, "SELECT 1 AS status")
        print(f"Resultado de teste: {rows}")
        return 0
    except (RuntimeError, SQLAlchemyError) as err:
        print(f"Falha ao conectar no banco: {err}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())