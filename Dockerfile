FROM python:3.13.0

# Prevent Python from writing .pyc files and ensure output is not buffered
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the application code, including the .env file
COPY . .

# Expose the application port
EXPOSE 8000