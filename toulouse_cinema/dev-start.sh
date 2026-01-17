#!/bin/bash
# Script to start development environment with hot-reload

set -e

echo "🚀 Starting development environment..."
echo "📝 This will start the frontend in development mode with hot-reload"
echo "🌐 The app will be available at http://localhost:3001"
echo "🔄 Changes to files will be automatically reflected"
echo ""
echo "⚠️  Production environment remains untouched and running"
echo ""

# Start development containers
docker-compose -f docker-compose.dev.yml up --build
