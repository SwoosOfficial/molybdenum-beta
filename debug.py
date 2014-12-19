def checkDiv(func):
	if "/" in func:
		lastOcc=0;
		while lastOcc != -1:
			checkFuncList = {};
			if "/(" in func:
				checkFunc=func[func.find("/(",lastOcc +1)+2:findBra(func,func.find("/(",lastOcc +1)) +1];
				checkFuncList[lastOcc]=checkFunc;
			else:
				checkFunc=func[func.find("/")+1];
				checkFuncList[lastOcc]=checkFunc;
			lastOcc=func.find("/",lastOcc +1);
#	elif "**(" or "**" in func:
#		lastOcc=0;
#		while lastOcc != -1:
#			checkFuncList = {};
#			if ")**(-1)" in func or ")**-1":
#				checkfunc=func[
opList=["+","-","/","*","|","^","%","&","_"];
alphaList=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",];
braList=["(",")","[","]","{","}","«","»","„","“"];
dotList=[".",","];
intLIst=["0","1","2","3","4","5","6","7","8","9"]
def corFunc(func):
	n=0;
	wordList=[]
	wordEndPos=0
	while n < len(func):
		getWord(func,wordEndPos,true,true);
		n+=1;
		n=max([n,wordEndPos]);

	checkPos=0;
	lastPosType="op";
	while checkPos < len(func):
		try:
			int(func[checkPos]);
			if lastPosType=="str":
				func=injectString(func,"*",checkPos);
			lastPosType="int";
			checkPos+=1;
		except ValueError:
			if func[checkPos] in dotList:
				if lastPosType == "op" or lastPosType == "bra":
					func=injectString(func,"0.",checkPos,1)
				elif lastPosType == "int" or lastPosType == "str":
					func=injectString(func,".",checkPos,1);
				elif lastPosType == "dot":
					func=ignoreString(func,checkPos);
			elif func[checkPos] in opList:
				if lastPosType == "op":
					if func[checkPos] == "+":
						func=ignoreString(func,checkPos)
					elif func[checkPos] == "-":
						if checkPos > 0:
							if func[checkPos-1] == "+":
								func=ignoreString(func,checkPos-1);
							elif func[checkPos-1] == "-":
								func=injectString(func,"+",checkPos-1,2);
							elif func[checkPos-1] == "/":
								if func[checkPos+1] == "(":
									varBraPos=findBra(func,checkPos+1);
									varInj="((-1)*"+func[checkPos+1:varBraPos+1]+")"
									func=injectString(func,varInj,checkPos,,varBraPos+1);
								elif func[checkPos+1] in intList:
									varInj="(-"+func[checkPos+1]+")";
									func=injectString(func,varInj,checkPos,1);
								elif func[checkPos+1] in alphaList +dotList
									
def injectString(string,injection,start,ignore=0,end=0):
	if end == 0:
		end=ignore+start;
	string=string[:start]+injection+string[end:];
	return string;
def ignoreString(string,start,ignore=1):
	end=start+ignore;
	string=string[:start]+string[end:];
	return string;

def getWord(string,pos=0,dot=false,global=false):
	word="";
	if dot:
		try:
			while string[pos] in alphaList +dotList:
				word+=string[pos];
				pos+=1;
		except IndexError:
			print("Hallo");
	else:
		try:
			while string[pos] in alphaList:
				word+=string[pos];
				pos+=1;
		except: IndexError
			print("Hallo");
	return word;

def findBra(string,braPos, braType="("):
	countBra=0;
	varBraPos=braPos;
	countSearch=0;
	if braType == "(":
		while string.find("(",varBraPos+1) < string.find(")",varBraPos+1) and string.find("(",varBraPos+1)!=-1:
			countBra=countBra +1;
			varBraPos=string.find("(",varBraPos+1);
		varBraPos=braPos
		while countBra >= countSearch:
			varBraPos=string.find(")",varBraPos+1);
			countSearch=countSearch+1;
		return varBraPos;
	elif braType == ")":
		revString=string[::-1];
		varBraPos=revBraPos=len(string)-1-braPos;
		while revString.find(")",varBraPos+1) < revString.find("(", varBraPos+1) and revString.find(")",varBraPos+1)!=-1:
			countBra=countBra +1;
			varBraPos=revString.find(")",varBraPos+1);
		varBraPos=revBraPos;
		while countBra >= countSearch:
			varBraPos=revString.find("(",varBraPos+1);
			countSearch=countSearch+1;
		varBraPos=len(string)-1-varBraPos;
		return varBraPos;
	else:
		raise NameError("BraType is invalid");
a="fuhuhuhuhu"
b=injectString(a,"bla",2)
print(b)