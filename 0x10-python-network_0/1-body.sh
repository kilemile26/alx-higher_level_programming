#!/bin/bash
# Use curl to send a GET request and display the body if the status code is 200
curl -s -w "%{http_code}" "$1"
