#!/bin/bash

echo "🚀 Starting Docker Compose (app + ollama)..."
docker-compose up -d --build

echo "⏳ Waiting for Ollama container to be running..."
until docker ps --filter "name=ollama" --filter "status=running" | grep ollama > /dev/null; do
  echo "🔄 Waiting for ollama service to become ready..."
  sleep 2
done

echo "📥 Pulling Mistral model into Ollama container..."
docker exec -it chatbotlaw-ollama-1 ollama pull mistral

echo "🧠 Starting Mistral model..."
docker exec -d chatbotlaw-ollama-1 ollama run mistral

echo "📡 Tailing all logs (app + ollama)..."
echo "🔻 Press Ctrl+C to exit logs view (services will keep running)"
docker-compose logs -f
