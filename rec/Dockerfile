FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose the port that the application listens on.
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=recSystem.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the script to generate rules when the container launches
CMD ["python3", "recommend.py"]
