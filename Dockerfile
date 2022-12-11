FROM python:3.8

# Install necessary libraries
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

# Copy the bot code to the container
COPY cartoon_bot.py /app/

# Set the working directory to the app directory
WORKDIR /app/

# Run the bot
CMD ["python", "cartoon_bot.py"]
