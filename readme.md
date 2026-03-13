python -m venv movie
movie/Scripts/activate
pip freeze > requirements.txt
pip install -r requirements.txt. # if already have requirments.txt
# INSTALL MODULE
pip install fastapi
pip install uvicorn
pip install python-dotenv
pip install sqlalchemy
pip install mysql-connector or pip install pymysql
pip install python-multipart
pip install pydantic-settings
pip install passlib # FOR encryption
pip install bcrypt #for window
pip install argon2-cffi
# RUN UVICORN SERVER    
uvicorn app.main:app --reload

# DB CONNECTION URL
#DATABASE URL
postgresql+psycopg://user:pass@localhost:5432/dbname
mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}


<!-- DATABASE_URL = (
    f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
) -->
