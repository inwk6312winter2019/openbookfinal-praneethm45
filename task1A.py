fin = open('Book1.txt','r')
fin = fin.readlines()

""" subtask1  """
def unique_words(fin):
  res=[]
  for line in fin:
    line=line.strip()
    line=line.split()
    for word in line:
      if word not in res:
        res.append(word)
  print(res)
unique_words(fin)

""" subtask2 """
def count_the_article(fin):
  count=0
  for line in fin:
    line=line.strip()
    line=line.split()
    for word in line:
      count+=1
  print(count)
count_the_article(fin)

""" subtask3 """
def sorted_words(fin):
  res=[]
  ls=[]
  for line in fin:
    line=line.strip()
    line=line.split()
    for word in line:
      if word not in res:
        res.append(word)
  print(sorted(output[::-1], key = len))
sorted_words(fin)


""" subtask4 """
def character_word_count(fin):
  dic=dict()
  for line in fin:
    line=line.strip()
    line=line.lower()
    line=line.split()
    for word in line:
      if word not in dict1:
             dic[word]=1
      elif word in dic:
             dic[word]+=1
  print(dic)
character_word_count(fin)


""" subtask5 """

def starts_with_vow(fin):
  count=0
  vow=("a","e","i","o","u")
  for line in f1:
    line=line.strip()
    line=line.lower()
    line=line.split()
    for word in line:
      if word[0] in vow:
        count+=1
  print(count)
starts_with_vow(fin)
