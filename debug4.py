opList=["+","-","/","*","|","^","%","&","_"];
alphaList=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",];
braList=["(","[","{","«","„",")","]","}","»","“"];
braOpenList=braList[:5];
braCloseList=braList[5:];
dotList=[".",","];
intList=["0","1","2","3","4","5","6","7","8","9"];

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


def corFunc(func):
	
	checkPos=0;
	while checkPos < len(func):
		if func[checkPos]:
			if func[checkPos-1] in alphaList + braCloseList +:
				func=injectString(func,"*",checkPos);
			lastPosType="int";
			checkPos+=1;
		except ValueError:
			if func[checkPos] in dotList:
				if lastPosType == "op" or lastPosType in braOpenList:
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
									func=injectString(func,varInj,checkPos,0,varBraPos+1);
								elif func[checkPos+1] in intList:
									varInj="(-"+func[checkPos+1]+")";
									func=injectString(func,varInj,checkPos,1);
								elif func[checkPos+1] in alphaList +dotList:
                                                                        print("");

print(findAbs("||x|+|x+1||",1));
