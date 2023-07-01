#!/bin/bash
# Take a url using command line args and display the size of the body
curl -s "$1" | wc -c
