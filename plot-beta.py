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
#
# ------------------------------------------------------------------------------------------------------------------------------------------------
#
# 	Defining checkBra nd corBra
#
def checkBra(string);
	if string.count("(") != string.count(")"):
		print("There is a Bracket error in the given function!")
		corBra(string);

def corBra(string);
	print("I  am attempting to correct brackets errors...");
	braEndAdd = braBegAdd = 0;
	while string.count("(") > string.count(")"):
		string = string+")";
		braEndAdd=braEndAdd+1;
	while string.count("(") < string.count(")"):
		string = "("+ string;
	if braEndAdd != 0:
		print("I have added "+braEndAdd+" ')' at the end of the function.");
	elif braBegAdd !=0:
		print("I have added "+braBegAdd+" '(' at the beginning of the function.");
	conQuery=input(Countinue?);
	if conQuery not in yesList:
		noFunc();
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
#
#			 Handling bracket errors
#
	checkBra(func)
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

