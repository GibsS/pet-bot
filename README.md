# PET BOT

A bot that's a pet. The chat bot is implemented with a recurrent neural network using attention trained on the cornell movie dialogs corpus.

## Install

* Clone this repository:
```
git clone https://github.com/GibsS/pet-bot
```
* Install tensor flow v1.0.1 (there were problems with v1.1):

## Run

* Training: 
```
sh scripts/train.sh
```

* Talk:
``` 
sh scripts/talk.sh
```

The parameter of either can be changed but talk.sh must be run with the same parameters as the one used for training.sh