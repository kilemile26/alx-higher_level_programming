#!/bin/bash

# Check if the URL argument is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Use curl to get the response body and measure its size in bytes
response_size=$(curl -sI "$1" | grep -i Content-Length | awk '{print $2}' | tr -d '\r')

# Display the size of the response body
echo "$response_size"
