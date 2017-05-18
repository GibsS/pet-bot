# PET BOT

A bot that's a pet. The chat bot is implemented with a recurrent neural network using attention, trained on the cornell movie dialogues corpus.

## Install

* Clone this repository: *
```
git clone https://github.com/GibsS/pet-bot
```
* Install tensor flow v1.0.1 (to avoid problems with v1.1 or higher):

## Run

* Training:
```
sh scripts/train.sh
```

* Talk:
``` 
sh scripts/talk.sh
```

* Deploy server: (make sure you open port 5000)
```
sh scripts/server.sh
```

Their parameters can be changed (see translate.py for the complete list) but talk.sh and server.sh must be run with the same parameters as the one used for train.sh.
