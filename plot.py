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
default=1
yMin=-5;
yMax=5;
xMin=-5;
xMax=5;
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
typeAxList=["log","lin","linear","logartihmic"];
typeXExList=["typeX","Xtype","X-type","x-type","X-Type","x-Type","XType","xtype","typex","TypeX","Typex","type-x","type-X","Type-x","Type-X"];
typeYExList=["typeY","Ytype","Y-type","y-type","Y-Type","y-Type","YType","ytype","typey","TypeY","Typey","type-y","type-Y","Type-y","Type-Y"];
fNameExList=["name","filename","fname","Name","Filename","Fname","f-name","F-name","F-Name"];
yesList=["Y","y","1","yes","Yes","yo","Yo","True","true"];
#
#------------------------------------------------
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
		except exceptions.ValueError:
			print("There seem to be a problem with your function");
#
#
#			 yMin:
#
	elif list[0] in yMinExList:
		try:
			global yMin;
			yMin=int(list[1]);
		except exceptions.ValueError:
			print (list[0]+" has to be an integer");
#
#
#			 yMax:
#
	elif list[0] in yMaxExList:
		try:
			global yMax;
			yMax=int(list[1]);
		except exceptions.ValueError:
			print(list[0]+" has to be an integer");
#
#
#			 xMax:
#
	elif list[0] in xMaxExList:
		try:
			global xMax;
			xMax=int(list[1]);
		except exceptions.ValueError:
			print(list[0]+" has to be an integer");
#
#
#			 xMin:
#
	elif list[0] in xMinExList:
		try:
			global xMin;
			xMin=int(list[1]);
		except exceptions.ValueError:
			print(list[0]+" has to be an integer")	;
#
#
#			 Accuracy:
#
	elif list[0] in accuracyExList:
		try:
			global accuracy;
			accuracy=int(list[1]);
		except exceptions.ValueError:
			print(list[0]+" has to be an integer");
#
#
#			Size:
#
	elif list[0] in sizeExList:
		try:
			global size;
			size=int(list[1]);
		except exceptions.ValueError:
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
		if list[1] in typeYList:
			if list[1] in typeYlog:	
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
		print("Sorry i do not understand:"+list[0])
#
# ------------------------------------------------
#
# Gathering Input:
#
print("Comprehending the input...")
#
#	 Checking System Arguments:
#
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
else:
	print("I could not find any input...");
	func=input("Please give me a function: ");
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
			print("I could not find any input again...");
			print("I will use default values...");
			default=1;	
#
#
# Initialize dynamic variables:
#
funcPrefix="f(x)";
#
print("Plotting the function: "+funcPrefix+" = "+func);
#
#
# Inittialize the Axis variables:
#
if typeX == "lin":
	typeXGraph=graph.axis.linear(min=xMin, max=xMax);
else:
	typeXGraph=graph.axis.logarithmic(min=xMin, max=xMax);
if typeY == "lin":
	typeYGraph=graph.axis.linear(min=yMin, max=yMax);
else:
	typeYGraph=graph.axis.linear(min=yMin, max=yMax);
#
# ------------------------------------------------
#
# Setting up the canvas:
#
c=canvas.canvas();
#
# ------------------------------------------------
#
# Creating graph data
#
g=graph.graphxy(width=size, x=typeXGraph, y=typeYGraph);
#
# ------------------------------------------------
#
# Plotting:
#
plotZ= g.plot(graph.data.function("y(x)="+func, points=accuracy, context=locals()));
#
# ------------------------------------------------
#
# Writing PDF:
#
c.insert(g);
c.writePDFfile(fName);
os.system("evince "+fName+".pdf");