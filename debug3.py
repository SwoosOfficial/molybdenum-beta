opList=["+","-","/","*","|","^","%","&","_"];
alphaList=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",];
braList=["(","[","{","«","„",")","]","}","»","“"];
braOpenList=braList[:5];
braCloseList=braList[5:];
dotList=[".",","];
intList=["0","1","2","3","4","5","6","7","8","9"];
func="||x|+|x-1||/|x+1||";
fatalOn=True;
infoOn=[True,True,False,False];




print(func);
print(replaceAbs(func));
