#!/bin/sh
cd /home/peterworth/pet-bot/
python translate.py --data_dir train/ --train_dir train/ --from_train_data data/conversation_prompt.txt --to_train_data data/conversation_reply.txt
