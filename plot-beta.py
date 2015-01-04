#!/usr/bin/python3
#
#
#
#
# This is a simple plot script.
#
print("Initializing...")
#
#
# ------------------------------------------------
#
# First of all importing necessary packages:
#
try:
	import numpy as np;
	import scipy as sci;
	from scipy import constants;
	from pyx import *;
	import sys;
	import os;
except Exception as impExc:
	print("I could not find all necessary python- extensions (Numpy, Scipy and Pyx)"), impExc;
#
# ------------------------------------------------
#
# Setting default values:
#
eps=np.finfo(float).eps;
default=1;
yMin=eps;
xMax=5;
yMax=xMax;
xMin=eps;
accuracy=100;
size=15;
typeX="lin";
typeY="lin";
fName="Plot";
Carg=len(sys.argv)-1;
fatalOn=True;
infoOn=[True,True,False,False];
#
#------------------------------------------------
#
#Setting Comprehension Lists:
#
funcExList=["f(x)","f","F","F(x)","y(x)","y","Y","function","func","Function", "Func"];
yMinExList=["ymin","Ymin","YMin","yMin","y-Min","Y-Min","y-min","Y-min","y from","y-from","Y from","Y-from"];
xMinExList=["xmin","Xmin","XMin","xMin","x-Min","X-Min","x-min","X-min","from","x from","x-from","X-from","X from"];
yMaxExList=["ymax","Ymax","YMax","yMax","y-Max","Y-Max","y-max","Y-max","y to","y-to","Y-to","Y to"];
xMaxExList=["xmax","Xmax","XMax","xMax","x-Max","X-Max","x-max","X-max","to","x to","x-to","X-to","X to"];
accuracyExList=["accuracy","acc","points","Accuracy","Acc","Points"];
sizeExList=["size","Size"];
typeXlog=["log","logarithmic"];
typeAxList=["log","lin","linear","logartihmic"];
typeXExList=["typeX","Xtype","X-type","x-type","X-Type","x-Type","XType","xtype","typex","TypeX","Typex","type-x","type-X","Type-x","Type-X"];
typeYExList=["typeY","Ytype","Y-type","y-type","Y-Type","y-Type","YType","ytype","typey","TypeY","Typey","type-y","type-Y","Type-y","Type-Y"];
fNameExList=["name","filename","fname","Name","Filename","Fname","f-name","F-name","F-Name"];
yesList=["Y","y","1","yes","Yes","yo","Yo","True","true","yy"];
critFunc=["/","**","root","sqrt","log","arc"]
#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# Defining Comprehension Function:
#
def comprehendF(stringZ):
	list=stringZ.split("=");
#
#
#			 Function:
#
	if list[0] in funcExList:
		try:
			global func;
			func=list[1];
		except ValueError:
			print("There seem to be a problem with your function");
#
#
#			 yMin:
#
	elif list[0] in yMinExList:
		try:
			global yMin;
			yMin=float(list[1]);
		except ValueError:
			print (list[0]+" has to be a float");
#
#
#			 yMax:
#
	elif list[0] in yMaxExList:
		try:
			global yMax;
			yMax=float(list[1]);
		except ValueError:
			print(list[0]+" has to be a float");
#
#
#			 xMax:
#
	elif list[0] in xMaxExList:
		try:
			global xMax;
			xMax=float(list[1]);
		except ValueError:
			print(list[0]+" has to be a float");
#
#
#			 xMin:
#
	elif list[0] in xMinExList:
		try:
			global xMin;
			xMin=float(list[1]);
		except ValueError:
			print(list[0]+" has to be a float")	;
#
#
#			 Accuracy:
#
	elif list[0] in accuracyExList:
		try:
			global accuracy;
			accuracy=int(list[1]);
		except ValueError:
			print(list[0]+" has to be an integer");
#
#
#			Size:
#
	elif list[0] in sizeExList:
		try:
			global size;
			size=int(list[1]);
		except ValueError:
			print(list[0]+" has to be an integer");
#
#
#			 Type of X- axis:
#
	elif list[0] in typeXExList:
		if list[1] in typeAxList:
			if list[1] in typeXlog:	
				global typeX;
				typeX="log";
		else:
			print("I can't understand"+list[0]);
#
#
#			 Type of Y- axis:
#
	elif list[0] in typeYExList:
		if list[1] in typeAxList:
			if list[1] in typeXlog:	
				global typeY;
				typeY="log";
		else:
			print("I can't understand"+list[0]);
#
#
#			 Filename:
#
	elif list[0] in fNameExList:
		global fName;
		fName=list[1];
#
#
#			 Comprehension Fail:
#
	else:
		print("Sorry i do not understand: "+list[0])
#
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# Defining getVal
#
def getVal():
	defQuery=input("Do you want to use the default values? ");
	if defQuery in yesList:
		print("I will use default values...");
		default=1;
	else:
		lateArgs=input("Give me the values now: ");
		lateArgsList=lateArgs.split();
		lateArgsLen=len(lateArgsList);
		if lateArgsLen:
			n=0;
			default=0;
			while n < lateArgsLen:
				comprehendF(lateArgsList[n]);
				n=n+1;
		else:
			print("I could not find any input...");
			print("I will use default values...");
			default=1;	
#
# -----------------------------------------------------------------------------------------------------------------------------------------------
#
# Defining Tools
#
#
#	Defining findBra
# 	
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
#
# ------------------------------------------------------------------------------------------------------------------------------------------------
#
# 	Defining corBra
#
def corBra(string):
	n=0;	
	while n < len(braOpenList):
		string=string.replace(braOpenList[n],"(");
		n+=1;
	n=0;
	while n < len(braCloseList):
		string=string.replace(braCloseList[n],")");
		n+=1;
	if string.count("(") != string.count(")"):
		print("There is a Bracket error in the given function!")
		print("I  am attempting to correct brackets errors...");
		braEndAdd = braBegAdd = 0;
		while string.count("(") > string.count(")"):
			string = string+")";
			braEndAdd+=1;
		while string.count("(") < string.count(")"):
			string = "("+ string;
			braBegAdd+=1
		if braEndAdd != 0:
			print("I have added "+repr(braEndAdd)+" ')' at the end of the function.");
		elif braBegAdd !=0:
			print("I have added "+repr(braBegAdd)+" '(' at the beginning of the function.");
		else:
			raise NameError("Fatal Fail in corBra");
		conQuery=input("Countinue? ");
		if conQuery not in yesList:
			print("Goodbye");
			exit();
		else:
			return string;
#
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#	 Defining | replacer
#
def replaceAbs(string):
	if string.count("|"):
		if string.count("|")%2:
			string=string+"|";
			if infoOn[1] or infoOn[2]:
				print("There was an error in your '|' placing. I attempted to correct it by adding one '|' at the end of the given expression")
		n=0;
		while n<len(string):
			if string[n]=="|":
				pos=findAbs(string,n);
				if pos!=None:
					string=injectString(string,")",pos,1,0);
					string=injectString(string,"abs(",n,1,0);
			n+=1;
	return string;

def findAbs(string,pos):
	count=1;
	if pos==0:
		while pos<len(string): 
			nextPos=string.find("|",pos+1);	
			if nextPos>0:
				if count>0:
					count+=checkRowAbs(string,nextPos);
					pos=max(pos+1,nextPos);
				elif count==0:
					endPos=pos;
					break;
				elif fatalOn:	
					print("Fatal Error in findAbs! #1");
			elif nextPos==-1:
				if infoOn[3]:
					print("Found no further '|'");
				endPos=pos;
				break;
			elif fatalOn:
				print("Fatal Error in findAbs! #2");
		if infoOn[2]:
			print("Found '|' at "+repr(endPos));
		return endPos;
	elif string[pos-1] in opList+braList:
		while pos<len(string): 
			nextPos=string.find("|",pos+1);	
			if nextPos>0:
				if count>0:
					count+=checkRowAbs(string,nextPos);
					pos=max(pos+1,nextPos);
				elif count==0:
					endPos=pos;
					break;
				elif fatalOn:	
					print("Fatal Error in findAbs! #3");
			elif nextPos==-1:
				if infoOn[3]:
					print("Found no further '|'");
				endPos=pos;
				break;
			elif fatalOn:
				print("Fatal Error in findAbs! #4");	
		if infoOn[2]:
			print("Found '|' at "+repr(endPos));
		return endPos;
	elif infoOn[3]:
		print("Nothing done in findAbs!");

def checkRowAbs(string,nextPos,depth=0):
	if nextPos-1-depth<0:
		return 1;
	elif string[nextPos-1-depth] in opList+braList and string[nextPos-1-depth]!="|":
		return 1;
	elif string[nextPos-1-depth] in opList+braList and string[nextPos-1-depth]=="|":
		return checkRowAbs(string,nextPos,depth+1);
	else:
		return -1;
#
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# Simple String Operations
#
def injectString(string,injection,start,ignore=0,end=0):
	if end == 0:
		end=ignore+start;
	if infoOn[2]:
		print("Injected: "+injection+" at "+repr(start)+" with override until "+repr(end)+" in "+string);
	string=string[:start]+injection+string[end:];
	return string;

def ignoreString(string,start,ignore=1):
	end=start+ignore;
	if infoOn[2]:
		print("Ignored all characters from "+repr(start)+" to "+repr(end)+" in "+string);
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
#
# -----------------------------------------------------------------------------------------------------------------------------------------------------
#
# Defining corFunc
#
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


#
# -------------------------------------------------------------------------------------------------------------------------------------------------------
#
# Defining valiData
#
def valiData():
	print("Validating Data...");
	global xMin;
	global xMax;
	global yMin;
	global yMax;
	global func;
#
#
# 		Correcting wrong Input
#
	if xMin > xMax:		
		xMin,xMax = xMax,xMin;
	elif xMin == xMax:
		xMin=xMin-eps;
		xMax=xMax+eps;
	if yMin > yMax:		
		yMin,yMax = yMax,yMin;
	elif yMin == yMax:
		yMin=yMin-eps;
		yMax=yMax+eps;
#
#
#		Handling Problems with log scale	
#
	if typeX == "log":
		if xMin < 0:
			print("Your value area is not suitable for a logarithmic scale");
			print("Starting at x="+repr(eps));
			xMin=eps;
			xMax=abs(xMax);
	if typeY == "log":
		if yMin < 0:
			print("Your target area is not suitable for a logarithmic scale");
			print("Starting at y="+repr(eps));
			yMin=eps;
			yMax=abs(yMax);
#
#
#		Handling bracket errors
#
	func=checkBra(func);
#
#
#		Handling | functions
#
	func=replaceAbs(func);
#
#
#		Handling Operator errors
#
	func=func.replace("^","**");
	if string.find("%")>0:
		func=func.replace("%","*(100**(-1))");
		if infoOn[1]:
			print("I am interpreting '%' as 'percent'.") 
#
#
# 		Handling Function problems
#
	func=corFunc(func);
#
#
# 		Handling Function problems
#
	n=0
	while n <= len(critFunc)-1:
		if func.find(critFunc[n]) >= 0:
			if n <= 1:
				zeroDivH(func);
			elif n <= 4:
				logNegH(func);
			elif n == 5:
				arcInvH(func);
		n=n+1;
#
# --------------------------------------------------------------------------------------------------------------------------------------------------------
#
# Defining zeroDivH
#
#def zeroDivH(func):
#	global checkFunc;
#	if "/" in func:
#		if "/(" in func:
#			checkFunc=func[func.find("/(")+2:func[func.find("/("):].find(")")+1];
#		else:
#			checkFunc=func[func.find("/")+1];
#	elif "**-1" in func or "**(-1)" in func:
#		revFunc=func[::-1];
#		if ")**-1" in func:
#			revPos=len(func)-1-func.find(")**-1");
#			revBraPos=revFunc.find("(",revPos);
#			braPos=len(func)-1-revBraPos;
#			lastBraPos=func.find(")**-1");
#			checkFunc=func[braPos+1:lastBraPos];
#		elif "**-1" in func:
#			checkFunc=func[func.find("**-1")-1];
#		elif ")**(-1)" in func:
#			revPos=len(func)-1-func.find(")**(-1)");
#			revBraPos=revFunc.find("(",revPos);
#			braPos=len(func)-1-revBraPos;
#			lastBraPos=func.find(")**(-1)");
#			checkFunc=func[braPos+1:lastBraPos];
#		else:
#			checkFunc=func[func.find("**(-1)")-1];
#
# --------------------------------------------------------------------------------------------------------------------------------------------------------
#
# log
#
def logNegH(func):
	print("logNeg"+func);
#
# ---------------
#
# arc
#
def arcInvH(func):
	print("arcInv"+func);
#
# --------------------------------------------------------------------------------------------------------------------------------------------------------
#
# Defining noFunc
#
def noFunc():
	global func;
	global default;
	print("I could not find a suitable function to plot...");
	func=input("Please give me a function: ");
	getVal();
	valiData();
#
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# Defining defFunc
#
def defFunc():
	print("Creating the canvas...");
	global funcPrefix;
	global c;
	global g;
#
#
# 			Initialize dynamic variables:
#
	funcPrefix="f(x)";
#
#
# 			Inittialize the Axis variables:
#
	if typeX == "lin":
		typeXGraph=graph.axis.linear(min=xMin, max=xMax);
	else:
		typeXGraph=graph.axis.logarithmic(min=xMin, max=xMax);
	if typeY == "lin":
		typeYGraph=graph.axis.linear(min=yMin, max=yMax);
	else:
		typeYGraph=graph.axis.logarithmic(min=yMin, max=yMax);
#
#
# 			Setting up the canvas:
#
	c=canvas.canvas();
#
#
# 			Creating graphs
#
	g=graph.graphxy(width=size, x=typeXGraph, y=typeYGraph);
#
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# Defining plotFunc
#
def plotFunc():
	try:
		defFunc();
		plotZ= g.plot(graph.data.function("y(x)="+func, points=accuracy, context=locals()));
	except SyntaxError:
		print("I can't plot the function: "+funcPrefix+"="+func);
		noFunc();
		plotFunc();
#
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#
# Defining gatherInput()
#
#
#	 		Checking System Arguments:
#
def gatherInput():
#
#
# Gathering Input:
#
	print("Comprehending the input...")
	global default;
	if Carg:
		n=0;
		default=0;
		while n < Carg:
#
#
#		 Comprehension:
#
			comprehendF(sys.argv[n+1])
			n=n+1;
		try:	
			funcZ=func;
			valiData();
		except NameError:
			noFunc();
	else:
		noFunc();
#
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# Writing PDF:
#
def writePdf():
	print("Writing PDF...");
	global c;
	c.insert(g);
#	c.writePDFfile(fName);
#
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# Open the PDF:
#
def openPdf():
	global openQuery;
	print(fName+".pdf successfully created!");
	openQuery=input("Shall i open it with evince? ");
	if openQuery in yesList:
		os.system("nohup evince "+fName+".pdf 2>/dev/null &");
	else:
		print("Goodbye");
	exit();
#
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# Actual start of the Program
#
gatherInput();
plotFunc();
writePdf();
#origErr=sys.stderr;
#origOut=sys.stdout;
#sys.stdout="";
#sys.stderr="";
c.writePDFfile(fName);
#sys.stderr=origErr;
#sys.stdout=origOut;
openPdf();

