# Use an official Python runtime as a parent image
FROM python:3.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY httpd.conf /etc
COPY myhttplib /app/myhttplib
COPY requirements.txt /app
COPY setup.py /app
COPY main.py /app
COPY httptest /var/www/html

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
RUN pip install -e.

# Make port 80 available to the world outside this container
EXPOSE 80

# Run main.py when the container launches
CMD ["python", "main.py"]