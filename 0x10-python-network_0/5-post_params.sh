#!/bin/bash
# Displays the body of the response
curl -sX POST $1 -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD"
