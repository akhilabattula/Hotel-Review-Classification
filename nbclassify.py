'''
Created on Jan 31, 2016

@author: akhila
'''
import glob
import os
import sys
import re
from fileinput import FileInput
from collections import OrderedDict

filedir=sys.argv[1]
#dp=open("","r")
word_dict=OrderedDict()
with open('nbmodel.txt', 'r') as f:
    for line in f:
        values=line.split("\t")
        key=values[0]
        word_dict[key]=[]
        for val in values:
            if val!=key and val!='\n':
                word_dict[key].append(val)
print word_dict
pk=open("nboutput.txt","w+")
os.chdir(filedir)
for f in glob.glob("*.txt"):
    print f
    fp=open(f,"r")
    mydata=fp.read()
    letters_only = re.sub("[^a-zA-Z0-9-']", " ", mydata)
    words=[]
    lower_case = letters_only.lower()        # Convert to lower case
    words = lower_case.split()   
    temporary=[]
    nd=float(1)
    nt=float(1)
    pd=float(1)
    pt=float(1)
    for akhi in words:
        if akhi[0]=="'":
            akhi=akhi[1:]
        if akhi.endswith("'"):
            akhi=akhi[:-2]
        if akhi in word_dict.keys():
            #print f,akhi,"found"
            temporary=word_dict[akhi]
        if len(temporary)==4:
            nd=nd*float(temporary[0])
            nt=nt*float(temporary[1])
            pd=pd*float(temporary[2])
            pt=pt*float(temporary[3])
        else:
            print "akhi is",akhi
    d = {'nd': nd, 'nt': nt, 'pd': pd,'pt':pt}
    """ maxval=max(d, key=d.get)
    if maxval=='nd':
        pk.write("deceptive negative ")
        pk.write(filedir+"\\"+f)
        pk.write("\n")
    elif maxval=='nt':
        pk.write("truthful negative ")
        pk.write(filedir+"\\"+f)
        pk.write("\n")
    elif maxval=='pd':
        pk.write("deceptive positive ")
        pk.write(filedir+"\\"+f)
        pk.write("\n")
    else:
        pk.write("truthful positive ")
        pk.write(filedir+"\\"+f)
        pk.write("\n")"""
    if nd>nt:
        if pd>pt:
            pk.write("deceptive negative ")
            pk.write(filedir+"\\"+f)
            pk.write("\n")
        else:
            pk.write("truthful negative ")
            pk.write(filedir+"\\"+f)
            pk.write("\n")
    else:
        if  pd>pt:
            pk.write("deceptive positive ")
            pk.write(filedir+"\\"+f)
            pk.write("\n")     
        else:  
            pk.write("truthful positive ")
            pk.write(filedir+"\\"+f)
            pk.write("\n") 
            
        
        
    
            
            
        
        
    
    
    
