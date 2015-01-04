import scipy
from scipy import constants

# corFuncLists:

#	trigonometric:
sinList=["sin"];
cosList=["cos"];
tanList=["tan"];
arccosList=["arccos"];
arcsinList=["arcsin"];
arctanList=["arctan"];
cotList=["cot"];
cscList=["csc"];
secList=["sec"];
arccotList=["arccot"];
arccscList=["arccsc"];
arcsecList=["arcsec"];

#	hyperbolic:
coshList=["cosh"];
sinhList=["sinh"];
tanhList=["tanh"];
arccoshList=["arccosh"];
arcsinhList=["arcsinh"];
arctanhList=["arctanh"];
cothList=["coth"];
cschList=["csch"];
sechList=["sech"];
arccothList=["arccoth"];
arccschList=["arccsch"];
arcsechList=["arcsech"];

#	exponential/ logarithmic:
logList=["log","ln"];
expList=["exp","e"];
rootList=["root","rt"];

#	misc:
sgnList=["sgn"];
absList=["abs"];
minList=["min"];
maxList=["max"];
sqrtList=["sqrt"];

#	constants:
piList=["pi"];
goldenList=["golden"];
func="2*(sin(2*(arcsec(sin(22,22))))+cosh(5)+cos(3.8)*pi+root(3,53)"

# getSubFuncLists

opList=["+","-","/","*","|","^","%","&","_"];
alphaList=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",];
braList=["(","[","{","«","„",")","]","}","»","“"];
braOpenList=braList[:5];
braCloseList=braList[5:];
dotList=[".",","];
intList=["0","1","2","3","4","5","6","7","8","9"];
constantsList=piList +goldenList;

def corFunc(func):
	wordList=getSubFunc(func)[0];
	argList=getSubFunc(func)[1];
	posList=getSubFunc(func)[2];
	arg=argList;
	wordLenList=[];
	argLenList=[];
	constant=[False]*len(wordList)
	n=0;
	while n<len(wordList):
		wordLenList.append(len(wordList[n]));
		n+=1
	n=0;
	while n<len(argList):
		argLenList.append(len(argList[n]));
		n+=1
	n=0;
	while n<len(argList):
		argList[n]=corFunc(argList[n]);
		n+=1
	n=0;
	while n < len(wordList):
# Functions
#       Trigonometric:
		if wordList[n] in sinList:
			print("Interpreting "+wordList[n]+" as sine function (numpy.sin).");
			wordList[n] = "numpy.sin("+arg[n]+")";
		elif wordList[n] in cosList:
			print("Interpreting "+wordList[n]+" as cosine function (numpy.cos).");
			wordList[n] = "numpy.cos("+arg[n]+")";
		elif wordList[n] in tanList:
			print("Interpreting "+wordList[n]+" as tangent function (numpy.tan).");
			wordList[n] = "numpy.tan("+arg[n]+")";
		elif wordList[n] in arccosList:
			print("Interpreting "+wordList[n]+" as inverse cosine function (numpy.arccos).");
			wordList[n] = "numpy.arccos("+arg[n]+")";
		elif wordList[n] in arcsinList:
			print("Interpreting "+wordList[n]+" as inverse sine function (numpy.arcsin).");
			wordList[n] = "numpy.arcsin("+arg[n]+")";
		elif wordList[n] in arctanList:
			print("Interpreting "+wordList[n]+" as inverse tangent function (numpy.arctan).");
			wordList[n] = "numpy.arctan("+arg[n]+")";
		elif wordList[n] in cotList:
			print("Interpreting "+wordList[n]+" as cotangent function (1/numpy.tan).");
			wordList[n] = "numpy.reciprocal(numpy.tan("+arg[n]+"))";
		elif wordList[n] in cscList:
			print("Interpreting "+wordList[n]+" as cosecant function (1/numpy.sin).");
			wordList[n] = "numpy.reciprocal(numpy.sin("+arg[n]+"))";
		elif wordList[n] in secList:
			print("Interpreting "+wordList[n]+" as secant function (1/numpy.cos).");
			wordList[n] = "numpy.reciprocal(numpy.cos("+arg[n]+"))";
		elif wordList[n] in arccotList:
			print("Interpreting "+wordList[n]+" as inverse cotangent function (numpy.arctan(reciprocal()).");
			wordList[n] = "numpy.arctan(numpy.reciprocal("+arg[n]+"))";
		elif wordList[n] in arccscList:
			print("Interpreting "+wordList[n]+"as inverse cosecant function (numpy.arcsin(reciprocal()).");
			wordList[n] = "numpy.arcsin(numpy.reciprocal("+arg[n]+"))";
		elif wordList[n] in arcsecList:
			print("Interpreting "+wordList[n]+" as inverse secant function (numpy.arccos(reciprocal()).");
			wordList[n] = "numpy.arccos(numpy.reciprocal("+arg[n]+"))";
#       Hyperbolic:
		elif wordList[n] in coshList:
			print("Interpreting "+wordList[n]+" as cosine hyperbolicus function (numpy.cosh).");
			wordList[n] = "numpy.cosh("+arg[n]+")";
		elif wordList[n] in sinhList:
			print("Interpreting "+wordList[n]+" as sine hyperbolicus function (numpy.sinh).");
			wordList[n] = "numpy.sinh("+arg[n]+")";
		elif wordList[n] in tanhList:
			print("Interpreting "+wordList[n]+" as tangent hyperbolicus function (numpy.tanh).");
			wordList[n] = "numpy.tanh("+arg[n]+")";
		elif wordList[n] in arccoshList:
			print("Interpreting "+wordList[n]+" as inverse cosine hyperbolicus function (numpy.arccosh).");
			wordList[n] = "numpy.arccosh("+arg[n]+")";
		elif wordList[n] in arcsinhList:
			print("Interpreting "+wordList[n]+" as inverse sine hyperbolicus function (numpy.arcsinh).");
			wordList[n] = "numpy.arcsinh("+arg[n]+")";
		elif wordList[n] in arctanhList:
			print("Interpreting "+wordList[n]+" as inverse tangent hyperbolicus function (numpy.arctanh).");
			wordList[n] = "numpy.arctanh("+arg[n]+")";
		elif wordList[n] in cothList:
			print("Interpreting "+wordList[n]+" as cotangent hyperbolicus function (coth).");
			wordList[n] = "1+(2)/(-1+numpy.exp(2*("+arg[n]+")))";
		elif wordList[n] in sechList:
			print("Interpreting "+wordList[n]+" as secant hyperbolicus function (1/numpy.cosh).");
			wordList[n] = "numpy.reciprocal(numpy.cosh("+arg[n]+"))";
		elif wordList[n] in cschList:
			print("Interpreting "+wordList[n]+" as cossecant hyperbolicus function (csch).");
			wordList[n] = "(2*numpy.exp("+arg[n]+"))/(-1+numpy.exp(2*("+arg[n]+")))";
		elif wordList[n] in arccothList:
			print("Interpreting "+wordList[n]+" as inverse cotangent hyperbolicus function (arccoth).");
			wordList[n] = "numpy.arctanh(numpy.reciprocal("+arg[n]+"))";
		elif wordList[n] in arcsechList:
			print("Interpreting "+wordList[n]+" as inverse secant hyperbolicus function (arcsech).");
			wordList[n] = "numpy.arccosh(numpy.reciprocal("+arg[n]+"))";
		elif wordList[n] in arccschList:
			print("Interpreting "+wordList[n]+" as inverse cosecant hyperbolicus function (arccsch).");
			wordList[n] = "numpy.arcsinh(numpy.reciprocal("+arg[n]+"))";
#       Exponents and Logarithms:
		elif wordList[n] in logList:
			print("Interpreting "+wordList[n]+" as natural logarithm (numpy.log)");
			wordList[n] = "numpy.log("+arg[n]+")";
		elif wordList[n] in expList:
			print("Interpreting "+wordList[n]+" as exponential function (numpy.exp)");
			wordList[n] = "numpy.exp("+arg[n]+")";
		elif wordList[n] in rootList:
			rootType=arg[n].find(",");
			if rootType != -1:
				rootTier=arg[n][:rootType];
				rootArg=arg[n][rootType+1:];
			else:
				rootTier="2";
				rootArg=arg[n];
			print("Interpreting "+wordList[n]+"("+arg[n]+") as "+rootTier+"th root of "+rootArg+" (exp(("+rootTier+")^(-1)*log("+rootArg+")))");
			wordList[n]="numpy.exp(numpy.reciprocal("+rootTier+"*numpy.log("+rootArg+"))"
#       Misc:
		elif wordList[n] in sgnList:
			print("Interpreting "+wordList[n]+" as sign function (numpy.sign)");
			wordList[n] = "numpy.sign("+arg[n]+")";
		elif wordList[n] in absList:
			print("Interpreting "+wordList[n]+" as absolute value function (numpy.absolute)");
			wordList[n] = "numpy.absolute("+arg[n]+")";        
		elif wordList[n] in sqrtList:
			print("Interpreting "+wordList[n]+" as root function (sqrt)");
			wordList[n] = "numpy.sqrt("+arg[n]+")";
		elif wordList[n] in minList:
			print("Interpreting "+wordList[n]+" as minimum value function (numpy.minimum)");
			wordList[n] = "numpy.minimum("+arg[n]+")";
		elif wordList[n] in maxList:
			print("Interpreting "+wordList[n]+" as maximun value function (numpy.maximum)");
			wordList[n] = "numpy.maximum("+arg[n]+")";
#		elif wordList[n] in gaussList:
# Constants
		elif wordList[n] in piList:
			print("Interpreting "+wordList[n]+" as pi ("+repr(scipy.pi)+")");
			wordList[n] = "scipy.pi";
			constant[n]=True;
		elif wordList[n] in goldenList:
			print("Interpreting "+wordList[n]+" as golden ratio ("+repr(scipy.golden)+")");
			wordList[n] = "scipy.golden";
			contant[n]=True;
		n+=1
	n=0;
	while n<len(wordList):
#		print(str(posList[n]),str(wordLenList[n]),str(argLenList[n]));
		
#		print("injected "+wordList[n]+" ...");
#		print(func);
		if constant[n]:
			func=injectString(func,wordList[n],posList[n]-wordLenList[n],wordLenList[n]+argLenList[n]);
			posList=[x+(len(wordList[n])-wordLenList[n]-argLenList[n]) for x in posList];
		else:
			func=injectString(func,wordList[n],posList[n]-wordLenList[n],wordLenList[n]+argLenList[n]+2);
			posList=[x+(len(wordList[n])-wordLenList[n]-argLenList[n]-2) for x in posList];
		n+=1;
	return func;

def getSubFunc(func):
	n=0;
	wordEndPos=0;
	wordEndPosList=[];
	wordList=[]
	while n < len(func):
		try:
                        if getWord(func,n,1)[0] not in ["x","y","z"]+dotList:
                                wordList.append(getWord(func,n,1)[0]);
                                wordEndPos=getWord(func,n,1)[1];
                                wordEndPosList.append(wordEndPos);
		except TypeError:
			pass
		finally:
			if wordEndPos>n:
				n=wordEndPos;
				if func[n] in braOpenList:
					n=findBra(func,n)+1;
			else:
                                n+=1;
	posList=wordEndPosList;
	n=0;
	argList=[];
	while n<len(posList) and posList[n]<len(func):
		nextPosVal=func[posList[n]];
		if wordList[n] in expList:
			nextPosVal+=2;
		if nextPosVal in intList:
			argList.append(nextPosVal);
		elif nextPosVal in opList:
			if wordList[n] not in constantsList:
				argList.append("x");
			else:
				argList.append("");
		elif nextPosVal in braList:
			arg=func[posList[n]+1:findBra(func,posList[n])];
			argList.append(arg);
		else:
			print("Fatal Error in getArgs at "+repr(posList[n])+repr(n)+nextPosVal);
		n+=1;
	return [wordList,argList,posList];

def injectString(string,injection,start,ignore=0,end=0):
	if end == 0:
		end=ignore+start;
#	print(str(start),str(ignore),str(end))
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
			if word!="":
				return [word,pos];
	else:
		if len(string)>pos and string[pos] in alphaList:	
			word="";
			while string[pos] in alphaList:
				word+=string[pos];
				pos+=1;
			if word!="":
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


print(func)
print(corFunc(func));

