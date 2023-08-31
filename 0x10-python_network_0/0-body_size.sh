#!/usr/bin/bash
# sends a request to a URL, after it takes it in and display the size
# of the body of the response
curl -s "$1" | wc -c
