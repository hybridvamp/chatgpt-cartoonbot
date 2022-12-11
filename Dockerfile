FROM python:3.8-slim

# Install necessary libraries
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the bot's code
COPY cartoon_bot.py .

# Run the bot's code when the container starts
CMD ["python", "cartoon_bot.py"]
