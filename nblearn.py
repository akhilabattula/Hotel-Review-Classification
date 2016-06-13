'''
Created on Jan 28, 2016

@author: akhila
'''
from __future__ import division
import sys,os,re
import glob
from collections import OrderedDict


""" root = sys.argv[1]

for path, subdirs, files in os.walk(root):
    for name in files:
        print os.path.join(path, name) """
        
def get_immediate_subdirectories(a_dir):# this function to get the subdirectories in a given directory
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

a_dir1=sys.argv[1] #main parent folder which consists of 2 folders
#print "a_dir is",a_dir1
sub_dir=[]#contains positive and negative 
sub_sub_dir=OrderedDict()#contains sub directories inside positive and negative polarities i.e truthful or deceptive
sub_dir= get_immediate_subdirectories(a_dir1)
#print "sub_dir is",sub_dir
for a in sub_dir:
    #print a
    tmp=a
    a=a_dir1+"\\"+a
    #print a
    sub_sub_dir[tmp]= get_immediate_subdirectories(a)
#print "sub_sub_dir is",sub_sub_dir
"""rev_sub_sub_dir=OrderedDict()# stores child to parent directory tree i.e
#if truth belongs to negative or positive polarity
for k in sub_sub_dir:
    rev_sub_sub_dir[sub_sub_dir[k][0]]=k
    rev_sub_sub_dir[sub_sub_dir[k][1]]=k

print "rev_sub_sub_dir is",rev_sub_sub_dir"""
"""fold_dict={}
for i in sub_dir:
    for j in sub_sub_dir[i]:
        b=a_dir1+"\\"+i+"\\"+j
        fold_dict[j]=i
        fold_dict[j]=get_immediate_subdirectories(b)
print "fold_dict is",fold_dict"""
"""dp=open("allreadoutputs.txt","w+")
for c in fold_dict:
    for d in fold_dict[c]:
        #print a_dir1+"\\"+rev_sub_sub_dir[c]
        path= a_dir1+"\\"+rev_sub_sub_dir[c]+"\\"+c+"\\"+d
        os.chdir(path)
        for f in glob.glob("*.txt"):
            print(f)
            fp=open(f,"r")
            matter=fp.read()
            pk=matter.split()
            for p in pk:
                dp.write(p)
                dp.write("\n")"""
## first classifier---4 single class
dp=open("nbmodel.txt","w+")
four_classifier=OrderedDict()
folds=[]
filecounter=OrderedDict()
for t in sub_sub_dir:
    tmplist=""
    for k in sub_sub_dir[t]:
        p=t
        print "p here",p
        path=a_dir1+"\\"+t+"\\"+k
        folds=get_immediate_subdirectories(path)
        filecount=0# to get total number of documents in a class
        for jj in folds:
            path1=path+"\\"+jj
            os.chdir(path1)
            
            for f in glob.glob("*.txt"):
                filecount=filecount+1
                #print (filecount),f
                #dp.write("\n")
                fp=open(f,"r")
                matter=""
                matter=fp.read()
                #dp.write(matter)
                #print matter
                tmplist=tmplist+matter
        
            #print tmplist
            #dp.write(tmplist)
        #print "tmplist is",tmplist
        #dp.write(tmplist)
    filecounter[p]=filecount
    four_classifier[p]=tmplist

tmplist3=""
for t3 in sub_sub_dir:
    print "t3 is",t3
    for k3 in sub_sub_dir[t3]:
        p3=k3
        print "p here1111",p3
        path=a_dir1+"\\"+t3+"\\"+k3
        folds=get_immediate_subdirectories(path)
        
        filecount=0# to get total number of documents in a class
        for jj in folds:
            path1=path+"\\"+jj
            os.chdir(path1)
            
            for f in glob.glob("*.txt"):
                filecount=filecount+1
                #print (filecount),f
                #dp.write("\n")
                fp=open(f,"r")
                matter3=""
                matter3=fp.read()
                #dp.write(matter)
                #print matter
                tmplist3=tmplist3+matter3
        break  
    print "after break",t3,k3 
            #print tmplist
            #dp.write(tmplist)
        #print "tmplist is",tmplist
        #dp.write(tmplist)
filecounter[p3]=filecount
four_classifier[p3]=tmplist3

tmplist4=""
mainflag=False
subflag=False
for t3 in sub_sub_dir:
    for k3 in sub_sub_dir[t3]:
        if subflag!=False:
            p4=k3
            print "p is",p4
            path=a_dir1+"\\"+t3+"\\"+k3
            folds=get_immediate_subdirectories(path)
        
            filecount=0# to get total number of documents in a class
            for jj in folds:
                path1=path+"\\"+jj
                os.chdir(path1)
            
                for f in glob.glob("*.txt"):
                    filecount=filecount+1
                #print (filecount),f
                #dp.write("\n")
                    fp=open(f,"r")
                    matter4=""
                    matter4=fp.read()
                #dp.write(matter)
                #print matter
                    tmplist4=tmplist4+matter4
        else:
            subflag=True 
    subflag=False        #print tmplist
            #dp.write(tmplist)
        #print "tmplist is",tmplist
        #dp.write(tmplist)
filecounter[p4]=filecount
four_classifier[p4]=tmplist4
"""for k in four_classifier:
    dp.write(k)
    dp.write("\n")
    for naughty in four_classifier[k]:
        dp.write(naughty)
    dp.write("\n")"""
#print "\n"
#print"file counter is", filecounter
four_classifier1=OrderedDict()
for one in four_classifier:
    data=""
    for naughty in four_classifier[one]:
        data=data+naughty
        
    letters_only = re.sub("[^a-zA-Z0-9-']", " ", data)
    #dp.write(letters_only)
    words=[]
    lower_case = letters_only.lower()        # Convert to lower case
    words = lower_case.split()   
    #four_classifier[k]=None
    #fp1.write(letters_only)
    temporary=[]
    for akhi in words:
        if akhi[0]=="'":
            akhi=akhi[1:]
        if akhi.endswith("'"):
            akhi=akhi[:-2]
        temporary.append(akhi)
    four_classifier1[one]=temporary
            #fp1.write(k+"\n")
"""for pp in four_classifier1:
    dp.write(pp)   
    dp.write("\n")
    for qq in four_classifier1[pp]:
        dp.write(qq)
        dp.write("\t")
    dp.write("\n")""" 
       
unique_words=OrderedDict()  
word_count=OrderedDict()       
#print "hi" 
for some in  four_classifier1:
    #print some,"is",four_classifier1[some]
    templist=[]
    #word_count[some]={}
    word_count[some]=OrderedDict()
    for word in four_classifier1[some]:
        #dp.write(word)
        #dp.write("\n")
        
        if word not in templist:
            templist.append(word)
            #if word=='chicago':
                #print word
            #dp.write("tmplist is")
            #dp.write(templist)
            
            #word_count[some][word]=[]
            #word_count[some][word].append(0)
            #print "printing",word,word_count[some]
            word_count[some][word]=1# smoooothing
            #dp.write(word_count[k][word])
            #dp.write(count)
        else:
            #print("in else")
            #print "printing",word,word_count[some][word]
            #if word=='chicago':
                #print word
            word_count[some][word]=word_count[some][word]+1
            #print "printing",word,word_count[some][word]
        unique_words[some]=templist
#print "unique_words",unique_words   
"""for uniqwords in unique_words:
    for otherwords in unique_words[uniqwords]:
        dp.write(otherwords)
        dp.write("\n")"""
"""for lol in word_count:
    for onelol in word_count[lol]:
        #dp.write(word_count[lol])
        #dp.write("\t")
        dp.write(str(word_count[lol]))
        dp.write(str(word_count[lol][onelol]))
        dp.write("\n")"""
"""for lol in word_count:
    print lol,word_count[lol]
    print("\t")"""
prior_probablities_classes=OrderedDict()
for thing in filecounter:
    #print "thing is",thing
    sum1=0
    for otherthing in filecounter:
        sum1=sum1+filecounter[otherthing]
            #print "sum1 is",sum1
    prior_probablities_classes[thing]=filecounter[thing]/sum1  
    #print filecounter[thing],sum1
    #print "required prior probability is",prior_probablities_classes[thing]
        
print prior_probablities_classes 

negation_prior_probablities_classes=OrderedDict()
for something in prior_probablities_classes:
    negation_prior_probablities_classes[something]=1-prior_probablities_classes[something]
print negation_prior_probablities_classes
for lol1 in word_count:
    print len(word_count[lol1].keys())
#probabilities_word_count=OrderedDict()
"""for toy in word_count:
    
    for roy in word_count[toy]:
        val=0
        
        val=word_count[toy][roy]+1/"""
unique_wordlist=[]
for uword in unique_words:
    for vword in unique_words[uword]:
        unique_wordlist.append(vword)
#print unique_wordlist
final_list=OrderedDict()
"""for pqr in word_count:
    print pqr"""
     
for wrd in unique_wordlist:
    final_list[wrd]=[]
    
    for pqr in word_count:
        if wrd in word_count[pqr]:
            totsum=0
            for z in word_count[pqr]:
                totsum=totsum+word_count[pqr][z]
            ans=((word_count[pqr][wrd])+1)/((totsum)+len(unique_wordlist))
            final_list[wrd].append(ans)
        else:
            ans=(0+1)/(totsum+len(unique_wordlist))
            final_list[wrd].append(ans)
for a in  final_list:
    dp.write(str(a))
    print "a is",a
    dp.write("\t")
    for k in final_list[a]:
        dp.write(str(k))
        print "k is",k
        dp.write("\t")
    dp.write("\n")        
            
            
    
           
        
    

                
            
    