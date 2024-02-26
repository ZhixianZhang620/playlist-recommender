FROM python:3.8-slim

WORKDIR /app


COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port available to the world outside this container
# ENV PORT = 52007
# EXPOSE 52007
ENV FLASK_RUN_PORT=5000

# Run app.py when the container launches
CMD ["flask", "run", "--host", "0.0.0.0"]