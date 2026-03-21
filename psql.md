# Step 1 — Install PostgreSQL
sudo apt update
sudo apt install postgresql postgresql-contrib -y

# Start and enable PostgreSQL
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Verify it's running
sudo systemctl status postgresql

# Step 2 — Create DB User & Database
# Switch to postgres user
sudo -u postgres psql

# Inside psql shell, run these:
CREATE DATABASE linux_mgmt;
CREATE USER sadashiv WITH PASSWORD 'Sadashiv@123';
ALTER ROLE sadashiv SET client_encoding TO 'utf8';
ALTER ROLE sadashiv SET default_transaction_isolation TO 'read committed';
ALTER ROLE sadashiv SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE linux_mgmt TO sadashiv;
\q

Step 3 — Install psycopg2
bash# Inside your virtual environment
pip install psycopg2-binary

# Add to requirements.txt
pip freeze > requirements.txt

If psycopg2-binary fails, install system deps first:
bashsudo apt install libpq-dev python3-dev gcc -y
pip install psycopg2


Step 4 — Update settings.py
python# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'linux_mgmt',
        'USER': 'sadashiv',
        'PASSWORD': 'Sadashiv@123',
        'HOST': 'localhost',     # or '127.0.0.1'
        'PORT': '5432',
    }
}

# Step 5 — Run Migrations
bash# Apply all Django migrations to PostgreSQL
python manage.py migrate

# If you had data in MySQL, re-create superuser
python manage.py createsuperuser

Step 6 — Test Connection
bash# Open Django DB shell
python manage.py dbshell

Not production but for dev and test
ALTER USER sadashiv SUPERUSER;
ALTER USER sadashiv CREATEROLE;

psql -U sadashiv -d linux_mgmt -h localhost

Create Table Query
sqlCREATE TABLE users (
    id          SERIAL PRIMARY KEY,
    username    VARCHAR(150)  NOT NULL UNIQUE,
    email       VARCHAR(255)  NOT NULL UNIQUE,
    password    VARCHAR(255)  NOT NULL,
    website     VARCHAR(500),
    created_at  TIMESTAMP     DEFAULT CURRENT_TIMESTAMP,
    updated_at  TIMESTAMP     DEFAULT CURRENT_TIMESTAMP
);

docker-compose exec db psql -U sadashiv -d linux_mgmt
