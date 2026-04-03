# Database Connection Template

Basic template to test and use a SQLAlchemy database connection using `DATABASE_URL`.

## Requirements

- Python 3.10+
- SQLAlchemy

Install dependencies:

```bash
pip install sqlalchemy
```

If you use a specific database, also install its driver:

- PostgreSQL: `pip install "psycopg[binary]"`
- MySQL: `pip install pymysql`
- SQL Server: `pip install pyodbc`

## Configure `DATABASE_URL`

Set the environment variable before running:

### Linux / macOS

```bash
export DATABASE_URL="sqlite:///./app.db"
```

### Windows (PowerShell)

```powershell
$env:DATABASE_URL="sqlite:///./app.db"
```

Examples:

- SQLite: `sqlite:///./app.db`
- PostgreSQL: `postgresql+psycopg://user:password@localhost:5432/my_database`
- MySQL: `mysql+pymysql://user:password@localhost:3306/my_database`
- SQL Server: `mssql+pyodbc://user:password@server:1433/my_database?driver=ODBC+Driver+18+for+SQL+Server&Encrypt=yes&TrustServerCertificate=yes`

## Run

```bash
python db_template.py
```

Expected output on success (current script messages):

- `Conexao OK` (exact current script output; means "Connection OK")
- `Resultado de teste: [...]` (Test result: [...])

## What this script provides

- `create_db_engine(...)`: creates SQLAlchemy engine
- `test_connection(engine)`: validates connectivity with `SELECT 1`
- `fetch_all(engine, query, params)`: runs a query and returns rows as dictionaries
- `execute_non_query(engine, query, params)`: runs insert/update/delete and returns affected rows
