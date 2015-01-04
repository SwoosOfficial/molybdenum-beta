braList=["(","[","{","«","„",")","]","}","»","“"];
braOpenList=braList[:5];
braCloseList=braList[5:];
yesList=["Y","y","1","yes","Yes","yo","Yo","True","true","yy"];
string="(({[))";

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

print(corBra(string));