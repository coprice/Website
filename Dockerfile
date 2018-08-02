# Use an official Python runtime as a parent image
FROM python:3.6

# Set the working directory to /
WORKDIR /

# Copy the current directory contents into the container at /
ADD . /

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
# ENV ENVIRONMENT production

# Run app.py when the container launches
CMD ["python3", "main.py"]
