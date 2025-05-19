# Start with your base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy everything
COPY . .

# Make start.sh executable
RUN chmod +x start.sh

# Install dependencies (if any)
RUN pip install -r requirements.txt

# Use start.sh as the container entry point
CMD ["./start.sh"]
