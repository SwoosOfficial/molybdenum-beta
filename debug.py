opList=["+","-","/","*","|","^","%","&","_"];
alphaList=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",];
braList=["(","[","{","«","„",")","]","}","»","“"];
braOpenList=braList[:5];
braCloseList=braList[5:];
dotList=[".",","];
intList=["0","1","2","3","4","5","6","7","8","9"];
funcDepth=-1;
								
def getSubFunc(func):
	n=0;
	wordEndPos=0;
	wordEndPosList=[];
	wordList=[]
	while n < len(func):
		try:
                        if getWord(func,n,1)[0] not in ["x","y","z","."]:
                                wordList.append(getWord(func,n,1)[0]);
                                wordEndPos=getWord(func,n,1)[1];
                                wordEndPosList.append(wordEndPos);
		except TypeError:
			pass
		finally:
			if wordEndPos>n:
				n=wordEndPos;
			else:
				n+=1;
	return [wordList,wordEndPosList];

def getArgs(posList):
        n=0;
        argList=[];
        while n<len(posList) and posList[n]<len(func):
                nextPosVal=func[posList[n]];
                if nextPosVal in intList:
                        argList.append(nextPosVal);
                elif nextPosVal in opList:
                        argList.append("x");
                elif nextPosVal in braList:
                        arg=func[posList[n]+1:findBra(func,posList[n])];
                        argList.append(arg);
                else:
                        print("Fatal Error in getArgs"+repr(n)+nextPosVal);
                n+=1;
        return argList;


def injectString(string,injection,start,ignore=0,end=0):
	if end == 0:
		end=ignore+start;
	string=string[:start]+injection+string[end:];
	return string;

def ignoreString(string,start,ignore=1):
	end=start+ignore;
	string=string[:start]+string[end:];
	return string;

def getWord(string,pos=0,dot=0):
	if dot:
		if len(string)>pos and string[pos] in alphaList +dotList:	
			word="";
			while len(string)>pos and string[pos] in alphaList + dotList:
				word+=string[pos];
				pos+=1;
			return [word,pos];
	else:
		if len(string)>pos and string[pos] in alphaList:	
			word="";
			while string[pos] in alphaList:
				word+=string[pos];
				pos+=1;
			return [word,pos];
def findBra(string, braPos):
        braType=string[braPos];
        try:
                braListPos=braList.index(braType);
        except ValueError:
                print(braType+" is not a bracket.");
        if braListPos<5:
                endPos=braPos;
                matchBra=braCloseList[braListPos];
                while string.count(matchBra, braPos, endPos+1)!=string.count(braType, braPos, endPos+1):
                        endPos+=1;
                return endPos;
        else:
                startPos=braPos;
                matchBra=braOpenList[braListPos-5];
                while string.count(matchBra, startPos, braPos+1)!=string.count(braType, startPos, braPos+1):
                       startPos-=1;
                return startPos;

func="2*(sin(2*(cos(222)))+cosh(5)+cos(3.8))"
print(func)
print(getArgs(getSubFunc(func)[1]));
