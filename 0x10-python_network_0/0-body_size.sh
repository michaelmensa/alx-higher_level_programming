#!/usr/bin/bash
# sends a request to a URL, after it takes it in and display the size
curl -s "$1" | wc -c
