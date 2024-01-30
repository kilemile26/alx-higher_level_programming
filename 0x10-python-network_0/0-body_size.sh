#!/bin/bash
# Use curl to get the response body and measure its size in bytes
curl -sI "$1" | grep -i Content-Length | awk '{print $2}' | tr -d '\r'
