# Minimal production Dockerfile

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11-slim

# Set the working directory
WORKDIR /app  

# Copy the requirements file
COPY requirements.txt /app/requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy the application code
COPY ./app /app/app 


# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

#  http://localhost:8080/