#!/bin/bash
# Use curl to get the response body and measure its size in bytes
curl -s "$1" | wc -c
