# Mailbox API

A simple FastAPI-based mailbox API for managing and sending emails. This mailbox system using Kafka involves building a scalable and efficient messaging system where users can send, receive, and store messages.

## Features

- Send emails via API endpoints
- Manage mailbox data
- FastAPI backend

## Requirements

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/mailbox_api.git
    cd mailbox_api
    ```

2. **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the API

```bash
uvicorn main:app --reload
```

- The API will be available at: [http://localhost:8000](http://localhost:8000)
- Interactive docs: [http://localhost:8000/docs](http://localhost:8000/docs)

## Configuration

- Edit `config.py` or environment variables as needed for email settings.

## Running Kafka and Redis (Cache)

To enable email queuing and caching, you may need to run Kafka and Redis:

### Start Kafka (using Docker)

```bash
docker run -d --name kafka -p 9092:9092 -e KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181 -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 bitnami/kafka:latest
```

> **Note:** You may also need to run Zookeeper:
>
> ```bash
> docker run -d --name zookeeper -p 2181:2181 bitnami/zookeeper:latest
> ```

### Start Redis (using Docker)

```bash
docker run -d --name redis -p 6379:6379 redis:latest
```

Make sure your application is configured to connect to these services as needed.

## Running Kafka and Redis (Without Docker)

If you prefer not to use Docker, you can run Kafka and Redis directly on your system:

### Install and Start Zookeeper

Kafka requires Zookeeper. Download and extract [Apache Zookeeper](https://zookeeper.apache.org/releases.html):

```bash
tar -xzf apache-zookeeper-*.tar.gz
cd apache-zookeeper-*/
bin/zkServer.sh start
```

or 

```bash
cd kafka_2.13-3.6.1
bin/zookeeper-server-start.sh config/zookeeper.properties
```

### Install and Start Kafka

Download and extract [Apache Kafka](https://kafka.apache.org/downloads):

```bash
tar -xzf kafka_*.tgz
cd kafka_*/
bin/kafka-server-start.sh config/server.properties
```

or

```bash
cd kafka_2.13-3.6.1
bin/kafka-server-start.sh config/server.properties
```

### Install and Start Redis

Install Redis using your package manager:

- **Ubuntu/Debian:**
    ```bash
    sudo apt update
    sudo apt install redis-server
    sudo systemctl start redis
    ```
- **macOS (with Homebrew):**
    ```bash
    brew install redis
    brew services start redis
    ```

Refer to the official documentation for more details on configuration and management.

## Alembic Setup

Alembic is used for handling database migrations.

### a. Install Alembic

```bash
pip install alembic
alembic init alembic
```

### b. Configure Database URL

Edit `alembic.ini` and set your database URL:

```ini
sqlalchemy.url = postgresql://postgres:postgres@postgres:5432/mailbox_db
```

### c. Create and Apply Migrations

Generate and apply your initial migration:

```bash
alembic revision --autogenerate -m "init schema"
alembic upgrade head
```

## You need to run this app

### Run it without docker (Using linux OS)
First you have to run kafka 
```bash
cd kafka_2.13-3.6.1
bin/zookeeper-server-start.sh config/zookeeper.properties
```
```bash
cd kafka_2.13-3.6.1
bin/kafka-server-start.sh config/server.properties
```
Then you should start postgresql server and radis
```bash
    sudo systemctl start postgresql
    sudo systemctl start redis
```
Now You can run your FastApi App
* Go to you python venv
```bash
    source venv/bin/activate
```
* Run your app
```bash
    uvicorn app.main:app --reload
```
Then you should run your kafka consumer service
* Go to you python venv and then
```bash
    python consumer_service.py
```
Now you test your FastApi mailbox app using below url
- The API will be available at: [http://localhost:8000](http://localhost:8000)
- Interactive docs: [http://localhost:8000/docs](http://localhost:8000/docs)

## License

MIT License
