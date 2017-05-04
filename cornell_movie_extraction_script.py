from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

conversation_path = "data/cornell_movie_dialogs_corpus/movie_conversations.txt"
line_path = "data/cornell_movie_dialogs_corpus/movie_lines.txt"

from_path = "data/conversation_prompt.txt"
to_path = "data/conversation_reply.txt"

def getCornellText():
    """
    RETURNS:
        a tuple (conversations, lines) where both are represented by line arrays
    """
    with open(conversation_path, "rb") as new_file:
        conversations = new_file.read().split('\n')
    with open(line_path, "rb") as new_file:
        lines = new_file.read().split('\n')

    return (conversations, lines)

def conversationToIdList(conversation_line):
    split = conversation_line.split(" +++$+++ ")

    if len(split) == 4:
        ids_text = split[3]

        ids = []
        num_start = -1
        for i, c in enumerate(ids_text):
            if c == 'L':
                num_start = i
            elif c == '\'' and num_start != -1:
                ids.append(ids_text[num_start:i])
                num_start = -1
        return ids

def conversationIdListToPairs(conversation_ids):
    pairs = []
    for i in range(len(conversation_ids)-1):
        pairs.append((conversation_ids[i], conversation_ids[i+1]))
    return pairs

def lineToText(line_line):
    split = line_line.split(" +++$+++ ")
    if len(split) == 5:
        return (split[0], split[4])
    else:
        return (-1, -1)

def generateData():
    convs, lines = getCornellText()

    # build dict of lines
    line_dict = dict()

    for line in lines:
        id, text = lineToText(line)
        if id != -1:
            line_dict[id] = text

    from_texts = []
    to_texts = []

    for conversation in convs:
        idList = conversationToIdList(conversation)
        if idList != None:
            for pair in conversationIdListToPairs(idList):
                from_texts.append(line_dict[pair[0]])
                to_texts.append(line_dict[pair[1]])

    with open(from_path, 'wb') as from_file:
        for line in from_texts:
            from_file.write(line + "\n")

    with open(to_path, 'wb') as to_file:
        for line in to_texts:
            to_file.write(line + "\n")

generateData()