# Use Python base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy application files
COPY . /app

RUN pip install --upgrade pip
# Install dependencies
RUN pip install flask


# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
