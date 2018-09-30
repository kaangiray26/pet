#!/usr/bin/python
#-*- encoding:utf-8 -*-
import os
import re
import taglib
from collections import OrderedDict

taglist=["TITLE","ARTIST","ALBUM","GENRE","TRACKNUMBER","DATE"]
cmdlist=["set","reset","help","save","exit"]
globaltags={"ARTIST":"","ALBUM":"","DATE":""}

os.system("clear && printf '\e[3J'")
print "PET\nAudio Metadata Editor"
print"1)Single File\n2)Folder"
ch1=input("\nSelect:")

def edit(path,gb):
  tags=OrderedDict([("TITLE",""),("ARTIST",""),("ALBUM",""),("GENRE",""),("DATE",""),("TRACKNUMBER","")])
  song = taglib.File(path)
  ###GLOBAL Edit
  for i in globaltags.keys():
    tags[i]=globaltags[i]
  trn=int(re.search(r'\d+', os.path.basename(path)).group())
  tags["TRACKNUMBER"]=trn
  ###
  while True:
    os.system("clear && printf '\e[3J'")
    print "[FILE]:[%s]" %(path)
    for i in tags.keys():
      print "[%s]:[%s]" %(i,tags[i])
    ui=raw_input("pet>")
    if ui not in cmdlist:
      print "Command not found. Try 'help' for command list"
      raw_input("return:")
    if ui=="help":
      print "Available commands:%s" %(cmdlist)
      raw_input("return:")
    if ui=="exit":
      exit()
    if ui=="set":
      print ">"
      for i in taglist:
        if tags[i] == "":
          data=raw_input("%s:" %(i))
          tags[i]=data
          if gb==1:
            if i=="ARTIST" or i=="ALBUM" or i=="DATE":
              globaltags[i]=data
    if ui=="save":
      for i in tags.keys():
        song.tags[i]=[tags[i]]
      song.save()
      print "done"
      return

if ch1==1:
  edit(raw_input("Path:").strip(),0)
elif ch1==2:
  location=raw_input("Path:").strip()
  os.chdir(location)
  songs=os.listdir(location)
  for i in songs:
    if i.startswith(".")==False:
        edit(os.path.abspath(i),1)
