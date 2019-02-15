import string

fin = open('Book1.txt')
file1 = fin.read()

def print_book(books):
	count=0
	dic=dict()
	dic1=dict()
	for line in books.split():
		word=line.strip(string.punctuation)
		myword=word.lower()
		count=count+1
		if myword not in dic:
			dic[myword]=1
		else:
			dic[myword]+=1

	print(' Number  of words in the Book is:',count)
	myls=[]
	for key,value in dic.items():
		myls.append((value,key))
	myls.sort(reverse=True)
	print("commonly used  20 words in Book are:")
	for freq,word in myls[:20]:
		print(word,freq,sep='\t')
	for char in myls[:20]:
		dic1[char]=dic1.get(char,0)+1
	print("\nDictionery containing the most common 20 words:\n")
	print(dic1)
fin=open('Book1.txt')
file1=fin.read()
fin1=open('Book2.txt')
file2=fin.read()
fin2=open('Book3.txt')
file3=fin.read()
print("conten in Book1")
print_book(file1)
print("content in Book2")
print_book(file2)
print("content in Book3")
print_book(file3)
