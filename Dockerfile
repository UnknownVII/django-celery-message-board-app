FROM python:3.13

# Prevents Python from writing .pyc files and ensures logs are unbuffered
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the app source code
COPY . .

# Copy the .env file into the container
COPY .env /app/.env

# Expose port 8000
EXPOSE 8000

# Run the application
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
