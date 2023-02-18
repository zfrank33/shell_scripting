#!/bin/bash

echo "Would you like to play a game of rock, paper, scissors?"
read answer

if [ "$answer" == "yes" ]; then
    python3 rock_paper_scissors.py
else
    echo "That's too bad, maybe next time."
fi
