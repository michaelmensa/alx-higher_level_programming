#!/bin/bash
# sends a JSON post request to a URL
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
