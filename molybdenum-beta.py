#!/usr/bin/python3
#
#
#
#
# This is a mathematic interpreter
#
#
#
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# First of all importing necessary packages:
#
try:
	import numpy;
	import scipy;
	from scipy import constants;
	from pyx import *;
	import sys;
	import os;
except Exception as impExc:
	print("I could not find all necessary python- extensions (Numpy, Scipy and Pyx)"), impExc;
#
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#	Setting default values:
#
#		Mathematics
#
defVariable="x";
defVariableList=["x","y","z"];
#
# 		SysOut
#
fatalOn=True;
infoOn=[True,True,True,True];
fatalOut=["Fatal Errors Occurred:",""];
defFatalLen=len(fatalOut[0]);
infoOut=["","","",""]
#
# 		TeX
#
logStyle="ln";
texLog="\\"+logStyle;
#
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#	Setting Comprehension Lists:
#
yesList=["Y","y","1","yes","Yes","yo","Yo","True","true","yy"];
#
#	corFuncLists:
#
#		trigonometric:
sinList=["sin","\\sin"];
cosList=["cos","\\cos"];
tanList=["tan","\\tan"];
arccosList=["arccos","\\arccos"];
arcsinList=["arcsin","\\arcsin"];
arctanList=["arctan","\\arctan"];
cotList=["cot","\\cot"];
cscList=["csc","\\csc"];
secList=["sec","\\sec"];
arccotList=["arccot","\\arccot"];
arccscList=["arccsc","\\arccsc"];
arcsecList=["arcsec","\\arcsec"];

#	hyperbolic:
coshList=["cosh","\\cosh"];
sinhList=["sinh","\\sinh"];
tanhList=["tanh","\\tanh"];
arccoshList=["arccosh","\\mathrm{arccosh}"];
arcsinhList=["arcsinh","\\mathrm{arcsinh}"];
arctanhList=["arctanh","\\mathrm{arctanh}"];
cothList=["coth","\\coth"];
cschList=["csch","\\csch"];
sechList=["sech","\sech"];
arccothList=["arccoth","\\mathrm{arccoth}"];
arccschList=["arccsch","\\mathrm{arccsch}"];
arcsechList=["arcsech","\\mathrm{arcsech}"];

#	exponential/ logarithmic:
logList=["log","ln","lg",texLog];
expList=["exp","e","\\exp"];
rootList=["root","rt","\\sqrt"];

#	misc:
sgnList=["sgn","\\sign"];
absList=["abs"];
minList=["min","\\min"];
maxList=["max","\\max"];
modList=["mod","%","\\mod"]
sqrtList=["sqrt"];
allFuncList=sqrtList+modList+maxList+minList+absList+sgnList+logList+expList+rootList+arcsechList+arccschList+arccothList+cothList+cschList+sechList+arccoshList+arcsinhList+arctanhList+sinhList+coshList+tanhList+sinList+cosList+tanList+arccosList+arcsinList+arctanList+cotList+cscList+secList+arccotList+arccscList+arcsecList;


#	constants:
piList=["pi","\\pi"];
goldenList=["golden"];
epsList=["eps","\\eps"];

#	varLists
varList=["xtype","logarithmic"];

#	logicLists
equalsList=["is","=","==","equals"];
notList=["not","!"];
logicLists=equalsList+notList;

#	commandLists
plotList=["plot"];
solveList=["solve"];
fitList=["fit"];
andList=["and"];
ifList=["for","if","while","with"];
printList=["tex"];
formatList=["format"];
nameList=["as"];
outputList=["output"];


commandListZ=plotList+solveList+fitList+andList+ifList+printList+formatList+nameList+outputList

# getSubFuncLists

opList=["+","-","/","*","|","^","%","&","_"];
alphaList=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];
braList=["(","[","{","«","„",")","]","}","»","“"];
braOpenList=braList[:5];
braCloseList=braList[5:];
defaultBraList=[braOpenList[0],braCloseList[0]]
dotList=[".",","];
intList=["0","1","2","3","4","5","6","7","8","9"];
constantsList=piList +goldenList+epsList;
#
#
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#
#
#	S T R I N G - S H I T
#
#
#
#
#
#
#
class FuncString(object):
    def __init__(self,funcString):
        self.funcString=funcString;
    def __str__(self):
        return self.funcString
#
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# Defining injectString(self)
#
# Requires:
#       Methods:
#           -
#       Parameters:
#           infoOut[]
#
    def injectString(self,injection,start,ignore=0,end=0):
        if end == 0:
            end=ignore+start;
            infoOut[2]+="\nI Injected: "+injection+" at "+repr(start)+" with override until "+repr(end)+" in "+self.funcString;
        self.funcString=self.funcString[:start]+injection+self.funcString[end:];
        return self.funcString;
#
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# Defining ignoreString(self)
#
# Requires:
#       Methods:
#           -
#       Parameters:
#           infoOut[]
#
    def ignoreString(self,start,ignore=1):
        end=start+ignore;
        infoOut[2]+="\nI Ignored all characters from "+repr(start)+" to "+repr(end)+" in "+self.funcString;
        self.funcString=self.funcString[:start]+self.funcString[end:];
        return self.funcString;
#
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# Defining getWord(self)
#
# Requires:
#       Methods:
#           -
#       Parameters:
#           infoOut[]
#
    def getWord(self,pos=0,addLists=[],removeLists=[]):
        checkList=addLists;
        originalPos=pos;
# - removelists to be added
        if len(self.funcString)>pos and self.funcString[pos] in checkList:	
            word="";
            while len(self.funcString)>pos and self.funcString[pos] in checkList:
                word+=self.funcString[pos];
                pos+=1;
        if word!="":
            infoOut[2]+="\nI got the word: "+word+" at position: "+repr(originalPos);
            return [word,pos];
        else:
            infoOut[2]+="\nI got no word at position: "+repr(originalPos);
#
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# Defining findAbs(self)
#
# Requires:
#       Methods:
#           checkRowAbs(self)
#       Parameters:
#           infoOut[]
#
    def findAbs(self,pos):
        string=self.funcString
        count=1;
        if pos==0:
            while pos<len(string): 
                nextPos=string.find("|",pos+1);	
                if nextPos>0:
                    if count>0:
                        count+=self.checkRowAbs(nextPos);
                        pos=max(pos+1,nextPos);
                    elif count==0:
                        endPos=pos;
                        break;
                    else:
                        fatalOut[0]+="\nFatal Error in findAbs! (#0)";
                elif nextPos==-1:
                    infoOut[3]+="\nI found no further '|'";
                    endPos=pos;
                    break;
                else:
                    fatalOut[0]+="\nFatal Error in findAbs! (#1)";
            infoOut[2]+="\nI found '|' at "+repr(endPos);
            return endPos;
        elif string[pos-1] in opList+braOpenList:
            while pos<len(string): 
                nextPos=string.find("|",pos+1);	
                if nextPos>0:
                    if count>0:
                        count+=self.checkRowAbs(nextPos);
                        pos=max(pos+1,nextPos);
                    elif count==0:
                        endPos=pos;
                        break;
                    else:
                        fatalOut[0]+="\nFatal Error in findAbs! (#2)";
                elif nextPos==-1:
                    infoOut[3]+="\nI found no further '|'";
                    endPos=pos;
                    break;
                else:
                    fatalOut[0]+="\nFatal Error in findAbs! (#3)";	
            infoOut[2]+="\nI found '|' at "+repr(endPos);
            return endPos;
        else:
            infoOut[3]+="\nI have done nothing in findAbs!";
#
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# Defining checkRowAbs(self,nextPos)
#
# Requires:
#       Methods:
#           -
#       Parameters & Lists:
#           opList, braList
#
    def checkRowAbs(self,nextPos,depth=0):
        string=self.funcString;
        if nextPos-1-depth<0:
            return 1;
        elif string[nextPos-1-depth] in opList+braList and string[nextPos-1-depth]!="|":
            return 1;
        elif string[nextPos-1-depth] in opList+braList and string[nextPos-1-depth]=="|":
            return self.checkRowAbs(nextPos,depth+1);
        else:
            return -1;
#
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# 	Defining Tools (--> getSubFunc, --> corFunc, --> valiData)
#
#
#		Defining findBra (--> getSubFunc, --> corBra, --> findAbs, --> getTexArg)
# 	
def findBra(string, braPos):
	braType=string[braPos];
	try:
		braListPos=braList.index(braType);
	except:
		fatalOut[0]+="\nFatal Error in findBra (#0, "+braType+" is not a bracket.)";
		raise;
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
#
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#
#	C O U N T E R - S H I T
#
#
#
#
#
#
#
#
class Counter(object):
    count=0;
    def __init__(self):
        type(self).count+=1;
    def __del__(self):
        type(self).count-=1;
#
#
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#
#
#
#
#
#	F U N C T I O N - S H I T
#
#
#
#
#
#
#
#
#
#
#
class Function(Counter,FuncString):
# (de-) construct
    def __init__(self,func,state="natural",typeZ="explicit",varList=[],inDim=1,outDim=1):
        self.func=func;
        self.state=state;
        self.typeZ=typeZ;
        self.varList=varList;
        self.inDim=inDim;
        self.outDim=outDim;
        Counter.__init__(self);
    def __str__(self):
        return self.func;
    def __del__(self):
        Counter.__del__(self);
# methods
#
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# Defining corBra
#
# Requires:
#       Methods:
#           -
#       Parameters:
#           infoOut[]
#
    def corBra(self):
        string=self.func;
        if string.count("(") != string.count(")"):
            infoOut[1]+="\nThere is a Bracket error in the given function!";
            infoOut[1]+="\nI  am attempting to correct brackets errors...";
            braEndAdd = braBegAdd = 0;
            while string.count("(") > string.count(")"):
                string = string+")";
                braEndAdd+=1;
            while string.count("(") < string.count(")"):
                string = "("+ string;
                braBegAdd+=1
            if braEndAdd != 0:
                infoOut[1]+="\nI have added "+repr(braEndAdd)+" ')' at the end of the function.";
            elif braBegAdd !=0:
                infoOut[1]+="\nI have added "+repr(braBegAdd)+" '(' at the beginning of the function.";
            else:
                fatalOut[0]+="\nFatal Error in corBra (#0)";
        self.func=string;
#
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# Defining replaceAbs()
#
# Requires:
#       Methods:
#           findAbs
#       Parameters:
#           infoOut[]
#
#
    def replaceAbs(self):
        string=self.func;
        if string.count("|"):
            if string.count("|")%2:
                string=string+"|";
                infoOut[1]+="There was an error in your '|' placing.\nI attempted to correct it by adding one '|' at the end of the given expression";
            n=0;
            while n<len(string):
                if string[n]=="|":
                    string=FuncString(string);
                    pos=string.findAbs(n);
                    if pos!=None:
                        string.injectString(")",pos,1,0);
                        string.injectString("abs(",n,1,0);
                n+=1;
                string=str(string);
        self.func=string;
#
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# Defining valiData
#
# Requires:
#       Methods:
#           Function.corBra(self), Function.replaceAbs(self), Function.corFunc(self), Function.replaceBra(self), Function.removeSpaces(self)
#       Parameters:
#           infoOut[]
#   
#    
    def valiData(self):
        oriFunc=self.func;
        infoOut[1]+="\nI am validating the Dates";
#
#
#		Handling bracket errors
#
        self.corBra();
#
#
#		Handling | functions
#
        self.replaceAbs();
#
#
#		Handling Operator errors
#
        func=self.func;
        func=func.replace("^","**");
        if func.find("%")>0:
            func=func.replace("%","*(100**(-1))");
            infoOut[1]+="\nI am interpreting '%' as 'percent'.";
        self.func=func;
#
# 		Handling Function problems
#
#	func=corFunc(func);
#	func=replaceBra(func);
#	func=removeSpaces(func);
#	func=func.replace(",",".");
	infoOut[0]+="\nI am interpreting "+oriFunc+" as "+func;
#
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# 		Defining corBra (--> valiData)
#
def corBra(string):
	if string.count("(") != string.count(")"):
		infoOut[1]+="\nThere is a Bracket error in the given function!";
		infoOut[1]+="\nI  am attempting to correct brackets errors...";
		braEndAdd = braBegAdd = 0;
		while string.count("(") > string.count(")"):
			string = string+")";
			braEndAdd+=1;
		while string.count("(") < string.count(")"):
			string = "("+ string;
			braBegAdd+=1
		if braEndAdd != 0:
			infoOut[1]+="\nI have added "+repr(braEndAdd)+" ')' at the end of the function.";
		elif braBegAdd !=0:
			infoOut[1]+="\nI have added "+repr(braBegAdd)+" '(' at the beginning of the function.";
		else:
				fatalOut[0]+="\nFatal Error in corBra (#0)"
	return string;
#
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#		Defining replaceBra
#
def replaceBra(string):
	n=0;	
	while n < len(braOpenList):
		string=string.replace(braOpenList[n],"(");
		n+=1;
	n=0;
	while n < len(braCloseList):
		string=string.replace(braCloseList[n],")");
		n+=1;
	return string;

#
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# Defining space remover
#
def removeSpaces(func):
	func.replace(" ","");
	infoOut[3]+="\nI removed all Spaces";
	return func;

#
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#	Defining getTexArg(func,pos) (--> getSubfunc, <-- findBra, <= braOpenList, <-- getMultipleArg)
#
def getMultipleArg(func,pos,depth=0):
	nextPos=findBra(func,pos)+1
	arg=func[pos+1:nextPos-1];
	if func[nextPos] in braOpenList:
		arg=arg+","+getMultipleArg(func,nextPos)[0];
		depth+=2;
	return [arg,depth];
#
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# 	Defining getSubFunc( --> corFunc, --> texInFunc)
#
def getSubFunc(func):
	n=0;
	wordEndPos=0;
	wordEndPosList=[];
	wordList=[];
	while n < len(func):
		if getWord(func,n,alphaList+dotList+["\\"])[0] not in defVariableList+dotList and getWord(func,n,alphaList+dotList+["\\"])[0]!=None:
                        wordList.append(getWord(func,n,alphaList+dotList+["\\"])[0]);
                        wordEndPos=getWord(func,n,alphaList+dotList+["\\"])[1];
                        wordEndPosList.append(wordEndPos);
		if wordEndPos>n:
			n=wordEndPos;
			if len(func)>n:
				if func[n] in braOpenList:
					n=findBra(func,n)+1;
				else:
					n+=1;
	posList=wordEndPosList;
	argList=getArgs(posList,func,wordList)[0];
	braCountList=getArgs(posList,func,wordList)[1];
	return [wordList,argList,posList,braCountList];

def getArgs(posList,func,wordList,depth=0):	
	n=0;
	argList=[];
	braCountList=[];
	while n<len(posList):
		if  posList[n]+depth<len(func):
			nextPosVal=func[posList[n]+depth];
		else:
			nextPosVal="*";
		if nextPosVal:
			if wordList[n] in expList:
				nextPosVal+=2;
			if wordList[n] not in allFuncList:
				argList.append("");
				braCountList.append(0);
			elif nextPosVal in intList:
				argList.append(nextPosVal);
				braCountList.append(0);
			elif nextPosVal in opList:
				argList.append(defVariable);
				braCountList.append(2);
			elif nextPosVal in braList:
				if nextPosVal in braCloseList:
					arg=defVariable;
					braCountList.append(2);
				elif nextPosVal in defaultBraList:
					arg=func[posList[n]+1:findBra(func,posList[n])];
					braCountList.append(2);
				else:
					arg=getMultipleArg(func,posList[n],2)[0];
					braCountList.append(getMultipleArg(func,posList[n],2)[1]);
				argList.append(arg);
			else:
				fatalOut[0]+="\nFatal Error in getArgs at "+repr(posList[n])+repr(n)+nextPosVal;
		else:
			getArgs(posList,func,wordList,depth+1);
		n+=1;
	return [argList,braCountList]
#
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# Defining corFunc --> valiData
#
def corFunc(func):
	wordList=getSubFunc(func)[0];
	argList=getSubFunc(func)[1];
	posList=getSubFunc(func)[2];
	braCountList=getSubFunc(func)[3];
	arg=argList;
	wordLenList=[];
	argLenList=[];
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
			infoOut[1]+="\nI am interpreting "+wordList[n]+" as sine function (numpy.sin).";
			wordList[n] = "numpy.sin("+arg[n]+")";
		elif wordList[n] in cosList:
			infoOut[1]+="\nI am interpreting "+wordList[n]+" as cosine function (numpy.cos).";
			wordList[n] = "numpy.cos("+arg[n]+")";
		elif wordList[n] in tanList:
			infoOut[1]+="\nI am interpreting "+wordList[n]+" as tangent function (numpy.tan).";
			wordList[n] = "numpy.tan("+arg[n]+")";
		elif wordList[n] in arccosList:
			infoOut[1]+="\nI am interpreting "+wordList[n]+" as inverse cosine function (numpy.arccos).";
			wordList[n] = "numpy.arccos("+arg[n]+")";
		elif wordList[n] in arcsinList:
			infoOut[1]+="\nI am interpreting "+wordList[n]+" as inverse sine function (numpy.arcsin).";
			wordList[n] = "numpy.arcsin("+arg[n]+")";
		elif wordList[n] in arctanList:
			infoOut[1]+="\nI am interpreting "+wordList[n]+" as inverse tangent function (numpy.arctan).";
			wordList[n] = "numpy.arctan("+arg[n]+")";
		elif wordList[n] in cotList:
			infoOut[1]+="\nI am interpreting "+wordList[n]+" as cotangent function (1/numpy.tan).";
			wordList[n] = "numpy.reciprocal(numpy.tan("+arg[n]+"))";
		elif wordList[n] in cscList:
			infoOut[1]+="\nI am interpreting "+wordList[n]+" as cosecant function (1/numpy.sin).";
			wordList[n] = "numpy.reciprocal(numpy.sin("+arg[n]+"))";
		elif wordList[n] in secList:
			infoOut[1]+="\nI am interpreting "+wordList[n]+" as secant function (1/numpy.cos).";
			wordList[n] = "numpy.reciprocal(numpy.cos("+arg[n]+"))";
		elif wordList[n] in arccotList:
			infoOut[1]+="\nI am interpreting "+wordList[n]+" as inverse cotangent function (numpy.arctan(reciprocal()).";
			wordList[n] = "numpy.arctan(numpy.reciprocal("+arg[n]+"))";
		elif wordList[n] in arccscList:
			infoOut[1]+="\nI am interpreting "+wordList[n]+"as inverse cosecant function (numpy.arcsin(reciprocal()).";
			wordList[n] = "numpy.arcsin(numpy.reciprocal("+arg[n]+"))";
		elif wordList[n] in arcsecList:
			infoOut[1]+="\nI am interpreting "+wordList[n]+" as inverse secant function (numpy.arccos(reciprocal()).";
			wordList[n] = "numpy.arccos(numpy.reciprocal("+arg[n]+"))";
#       Hyperbolic:
		elif wordList[n] in coshList:
			infoOut[1]+="\nI am interpreting "+wordList[n]+" as cosine hyperbolicus function (numpy.cosh).";
			wordList[n] = "numpy.cosh("+arg[n]+")";
		elif wordList[n] in sinhList:
			infoOut[1]+="\nI am interpreting "+wordList[n]+" as sine hyperbolicus function (numpy.sinh).";
			wordList[n] = "numpy.sinh("+arg[n]+")";
		elif wordList[n] in tanhList:
			infoOut[1]+="\nI am iInterpreting "+wordList[n]+" as tangent hyperbolicus function (numpy.tanh).";
			wordList[n] = "numpy.tanh("+arg[n]+")";
		elif wordList[n] in arccoshList:
			infoOut[1]+="\nI am interpreting "+wordList[n]+" as inverse cosine hyperbolicus function (numpy.arccosh).";
			wordList[n] = "numpy.arccosh("+arg[n]+")";
		elif wordList[n] in arcsinhList:
			infoOut[1]+="\nI am interpreting "+wordList[n]+" as inverse sine hyperbolicus function (numpy.arcsinh).";
			wordList[n] = "numpy.arcsinh("+arg[n]+")";
		elif wordList[n] in arctanhList:
			infoOut[1]+="\nI am interpreting "+wordList[n]+" as inverse tangent hyperbolicus function (numpy.arctanh).";
			wordList[n] = "numpy.arctanh("+arg[n]+")";
		elif wordList[n] in cothList:
			infoOut[1]+="\nI am interpreting "+wordList[n]+" as cotangent hyperbolicus function (coth).";
			wordList[n] = "1+(2)/(-1+numpy.exp(2*("+arg[n]+")))";
		elif wordList[n] in sechList:
			infoOut[1]+="\nI am interpreting "+wordList[n]+" as secant hyperbolicus function (1/numpy.cosh).";
			wordList[n] = "numpy.reciprocal(numpy.cosh("+arg[n]+"))";
		elif wordList[n] in cschList:
			infoOut[1]+="\nI am interpreting "+wordList[n]+" as cossecant hyperbolicus function (csch).";
			wordList[n] = "(2*numpy.exp("+arg[n]+"))/(-1+numpy.exp(2*("+arg[n]+")))";
		elif wordList[n] in arccothList:
			infoOut[1]+="\nI am interpreting "+wordList[n]+" as inverse cotangent hyperbolicus function (arccoth).";
			wordList[n] = "numpy.arctanh(numpy.reciprocal("+arg[n]+"))";
		elif wordList[n] in arcsechList:
			infoOut[1]+="\nI am interpreting "+wordList[n]+" as inverse secant hyperbolicus function (arcsech).";
			wordList[n] = "numpy.arccosh(numpy.reciprocal("+arg[n]+"))";
		elif wordList[n] in arccschList:
			infoOut[1]+="\nI am interpreting "+wordList[n]+" as inverse cosecant hyperbolicus function (arccsch).";
			wordList[n] = "numpy.arcsinh(numpy.reciprocal("+arg[n]+"))";
#       Exponents and Logarithms:
		elif wordList[n] in logList:
			logType=arg[n].find(",");
			if logType != -1:
				logTier=arg[n][:logType];
				logArg=arg[n][logType+1:];
				infoOut[1]+="\nI am interpreting "+wordList[n]+" as logarithm to the base "+logTier+" of "+logArg+":\n	(numpy.log("+logArg+"))/(numpy.log("+logTier+"))";
				wordList[n]="(numpy.log(logArg))/(numpy.log(logTier))";
			else:
				infoOut[1]+="\nI am interpreting "+wordList[n]+" as natural logarithm (numpy.log)";
				wordList[n] = "numpy.log("+arg[n]+")";
		elif wordList[n] in expList:
			infoOut[1]+="\nI am interpreting "+wordList[n]+" as exponential function (numpy.exp)";
			wordList[n] = "numpy.exp("+arg[n]+")";
		elif wordList[n] in rootList:
			rootType=arg[n].find(",");
			if rootType != -1:
				rootTier=arg[n][:rootType];
				rootArg=arg[n][rootType+1:];
			else:
				rootTier="2";
				rootArg=arg[n];
				countEng="nd";
			if rootTier=="1":
				countEng="st";
			elif rootTier=="3":
				countEng="rd";
			else:
				countEng="th";
			infoOut[1]+="\nI am interpreting "+wordList[n]+"("+arg[n]+") as "+rootTier+countEng+" root of "+rootArg+" (exp(("+rootTier+")^(-1)*log("+rootArg+")))";
			wordList[n]="numpy.exp(numpy.reciprocal("+rootTier+"*numpy.log("+rootArg+")))";
#       Misc:
		elif wordList[n] in sgnList:
			infoOut[1]+="\nI am interpreting "+wordList[n]+" as sign function (numpy.sign)";
			wordList[n] = "numpy.sign("+arg[n]+")";
		elif wordList[n] in absList:
			infoOut[1]+="\nI am interpreting "+wordList[n]+" as absolute value function (numpy.absolute)";
			wordList[n] = "numpy.absolute("+arg[n]+")";        
		elif wordList[n] in sqrtList:
			infoOut[1]+="\nI am interpreting "+wordList[n]+" as root function (sqrt)";
			wordList[n] = "numpy.sqrt("+arg[n]+")";
		elif wordList[n] in minList:
			infoOut[1]+="\nI am interpreting "+wordList[n]+" as minimum value function (numpy.minimum)";
			wordList[n] = "numpy.minimum("+arg[n]+")";
		elif wordList[n] in maxList:
			infoOut[1]+="\nI am interpreting "+wordList[n]+" as maximun value function (numpy.maximum)";
			wordList[n] = "numpy.maximum("+arg[n]+")";
		elif wordList[n] in modList:
			infoOut[1]+="\nI am interpreting "+wordList[n]+" as modolo function (%)";
			wordList[n] = "numpy.maximum("+arg[n]+")";
# Constants
		elif wordList[n] in piList:
			infoOut[1]+="\nI am interpreting "+wordList[n]+" as pi ("+repr(scipy.constants.pi)+")";
			wordList[n] = "scipy.constants.pi";
		elif wordList[n] in goldenList:
			infoOut[1]+="\nI am interpreting "+wordList[n]+" as golden ratio ("+repr(scipy.constants.golden)+")";
			wordList[n] = "scipy.constants.golden";
		elif wordList[n] in epsList:
			pass;
# Other Commands
		else:
			infoOut[1]+="\nI left untouched: "+wordList[n];
			wordList[n]=wordList[n];
		n+=1;
	n=0;
	while n<len(wordList):
		func=injectString(func,wordList[n],posList[n]-wordLenList[n],wordLenList[n]+argLenList[n]+braCountList[n]);
		posList=[x+(len(wordList[n])-wordLenList[n]-argLenList[n]-braCountList[n]) for x in posList];
		n+=1;
	return func;
#
#
#
#
#   I N P U T - S H I T
#
#
#
#
#
#
#
#
#
#
#
#
#  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
#
#	Input Handler (=>func, <-- getWord, <= input, <=infoOut, <= allFuncList, <= constantsList)
#
def inputHandler(inputZ):
	inputX=[];
	thread=[];
	globalZ=[];
	if inputZ=="":
		infoOut[0]+="\nI have found no input.";
		inputZ=input("\nWhat do you want me to do? ");
		inputHandler(inputZ);
	else:
		command=getWord(inputZ,0,alphaList)[0];
		inputZ=ingoreString(inputZ,0,getWord(inputZ,0,alphaList)[1]);
		inputList=inputZ.split("&");
# examplary input: plot f=2x § x>0 & g=ln(x) § x>0 &§ xtype=log
		n=0
		while n<len(inputList):
			if inputList[n][0]=="§":
				globalZ.append(inputList[n][1:])
			else:
				subInput=inputList[n].split("§");
				thread.append([subInput[0],subInput[1:]]);
			n+=1;
	return thread;
#
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#	Comprehender (<-- inputHandler, <-- interpretCommand)
#
def comprehend(thread):
	n=0;
	while n*2<=len(thread):
		mainFuncList=[];
		sideFuncList=[];
		mainCommandList=[];
		sideCommandList=[];
		m=0
		while m<len(thread[n][1][0]):
			interpreterZ(thread,n,m,mainFuncList,sideFuncList,mainCommandList,sideCommandList)
		n+=1;
#
#
#
#
#
def interpreterZ(thread,n,m,mainFuncList,sideFuncList,mainCommandList,sideCommandList,l=0)
	commandList=thread[n][1][0][m];
	action=interpretCommand(commandList);
	thread[n][1][0][m]=action;
	if "plot" in action:
		if action.index("plot")==len(action)-1 and "and" not in action:
			mainCommandList.append("plot");
			mainFuncList.append(thread[n][1][1]);
			lastCommand="main";
		elif False:
			pass;
		elif action.index("fit")==len(action)-1:
			mainCommandList.append("fit");
			sideCommandList.append("plot");
			mainFuncList.append(thread[n][1][1]);
			lastCommand="main";
	elif False:
		pass;
	elif "fit" in action:
		pass;
	elif "solve" in action:
		pass;
	elif "for" in action:
		if action.index("for")==len(action)-1:
			sideFuncList.append(thread[n][1][1]);
			lastCommand="side";
		else:
			infoOut[1]+="\nI couldn't find a proper condition! So i skipped!";
	elif "and" in action:
		 		if action.index("and")==len(action)-1 and lastCommand=="side":
			sideCommandList.append(
	return [mainFunc,
#
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#	interpretCommand (<-- inputHandler, --> inputHandler, <= plotList, <= solveList, <= notList, <= addList)
#
def interpretCommand(commandList):
	n=0;
	action=[];
	while n<len(commandList):
		if commandList[n] in plotList:
			action.append("plot");
		elif commandList[n] in solveList:
			action.append("solve");
		elif commandList[n] in fitList:
			action.append("fit")
		elif commandList[n] in andList:
			action.append("and");
		elif commandList[n] in printList:
			action.append("tex");
		elif commandList[n] in formatList:
			action.append("format");
		elif commandList[n] in ifList:
			action.append("for");
		elif commandList[n] in nameList:
			action.append("name");
		elif commandList[n] in outputList:
			action.append("output");
		else:
			fatalOut+="Fatal Error in interpretCommand #0";
		n+=1;
#
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# Actual start of the Program
#
#func=input("What do you want me to do? ");
func="plot sin(2* cos( 2x)) § x<0 § xtype=logarithmic & sin(3) &§ output=fuu.pdf"
#valiData();
print(func);
sol=inputHandler(func);
if len(fatalOut[0])>defFatalLen:
	print(fatalOut[0]);
print(infoOut[0]);
print(infoOut[1]);
#sol=eval(func);
print(sol);
