#!/usr/bin/bash
# to send a request to a URL, after it takes it in and display the size
curl -s "$1" | wc -c
