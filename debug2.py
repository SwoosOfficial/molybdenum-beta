opList=["+","-","/","*","|","^","%","&","_"];
alphaList=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",];
braList=["(",")","[","]","{","}","«","»","„","“"];
dotList=[".",","];
intLIst=["0","1","2","3","4","5","6","7","8","9"]
def getSubFunc(func):
	n=0;
	wordList=[]
	wordEndPos=0
	while n < len(func):
		try:
			wordList.append(getWord(func,n,1)[0]);
			wordEndPos=getWord(func,n,1)[1];
		except TypeError:
			pass
		finally:
			if wordEndPos>n:
				n=wordEndPos;
			else:
				n+=1;
	return wordList;

def corSubFunc(func):
	n=0;
	wordList = getSubFunc(func);
	while n < len(wordList):
# Functions
		if wordList[n] in sinList:
		elif wordList[n] in cosList:
		elif wordList[n] in tanList:
		elif wordList[n] in logList:
		elif wordList[n] in expList:
		elif wordList[n] in sgnList:
		elif wordList[n] in absList:
		elif wordList[n] in arccosList:
		elif wordList[n] in arcsinList:
		elif wordList[n] in arctanList:
		elif wordList[n] in coshList:
		elif wordList[n] in sinhList:
		elif wordList[n] in tanhList:
		elif wordList[n] in 
# Constants
def getWord(string,pos=0,dot=0):
	if dot:
		if len(string)>pos and string[pos] in alphaList +dotList:	
			word="";
			while len(string)>pos and string[pos] in alphaList + dotList:
				word+=string[pos];
				pos+=1;
			return [word,pos];
	else:
		if len(string)>pos and string[pos] in alphaList +dotList:	
			word="";
			while string[pos] in alphaList:
				word+=string[pos];
				pos+=1;
			return [word,pos];

corFunc("sadjfk.f34k2dj28d")
print(len("sadjfk.f34k2dj28d"))