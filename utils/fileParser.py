#!/usr/bin/env python3

import csv

class FileParser:
  def __init__(self, path):
    self.path = path
    self.content = []

  def readTextfile(self):
    with open(self.path, "r", encoding='utf-8', errors='replace') as f:
      line = f.readline()
      while line:
        self.content.append(line.replace("\n", ""))
        line = f.readline()

  def readCSVfileRow(self, delimiter):
    with open(self.path, newline='') as csvfile:
       spamreader = csv.reader(csvfile, delimiter=delimiter, quotechar='|')
       for row in spamreader:
          self.content.append(row)

  def readCSVfileCol(self, delimiter):
    with open(self.path, newline='') as csvfile:
       spamreader = csv.reader(csvfile, delimiter=delimiter, quotechar='|')
       tab = [[]]
       for row in spamreader:
         for i in range(0, len(row)):
           try:
             tab[i].append(row[i])
           except:
             tab.append([row[i]])
       self.content = tab