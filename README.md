Car Task API
---

**Technology Stack**:

- **Python 3.11**
- **FastAPI** – API building framework
- **SQLAlchemy 2** – ORM
- **Pydantic** – Data validation
- **Alembic** - Database migration system
- **PostgreSQL** – Database solution
- **Docker** & **Docker Compose** – Containerization and easy deployment

## Setup and Launch

There are 2 ways to set up and launch the project:
- [Through Docker](#Launch---The-Dockerized-way)
- [Manually](#Launch---The-Vanilla-way)

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/car-marketplace-api.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd car-marketplace-api
   ```
3. **Specify settings in the `.env` file**:
   ```env
   DB_HOST=address
   DB_PORT=123
   DB_NAME=name
   DB_USER=user
   DB_PASS=pwd
4. ```

### Launch - The Dockerized way:

3. **Install Docker and Docker Compose**, if you haven’t already

   [Add links]

4. **Change host and port** with needed values **in Dockerfile**!

   ```Dockerfile
   ...
   ENTRYPOINT ["uvicorn", "main:app", "--host", "THE HOST YOU WANT (0.0.0.0)", "--port", "THE PORT YOU WANT (8000)"]
   ```

5. **Start the project**:

   ```bash
   docker-compose up --build
   ```
6. !!! **Create migration and upgrade the db**, or db won't work !!!!:
   ```bash
   sudo docker-compose exec app alembic revision --autogenerate 
   sudo docker-compose exec app alembic upgrade head
   ```
    - If you have problems mentioning `revision id`, than your database is not clear.
      To reset alembic versions and force the migration, drop the table from your postgresql DB:
   ```sql
    DROP TABLE alembic_version
   ```
   And now you can try step 6 again.

### Launch - The "Vanilla" way:

3. **Create a python venv**:
   ```bash
   python -m venv venv
   ```

4. **Activate the venv**:
    - Windows
   ```bash
   # In cmd.exe
   venv\Scripts\activate.bat
   # In PowerShell
   venv\Scripts\Activate.ps1
   ```
    - MacOS, Linux:
   ```bash
   source myvenv/bin/activate
   ```
5. **Setup your postgresql server**, if you haven't already

   [Add links]
   
6. **Run the code**
   ```bash
   python main.py
   ```

---


Once setup is complete, you can access the API server at http://localhost:8000 by default.


