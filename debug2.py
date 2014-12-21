opList=["+","-","/","*","|","^","%","&","_"];
alphaList=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",];
braList=["(",")","[","]","{","}","«","»","„","“"];
dotList=[".",","];
intList=["0","1","2","3","4","5","6","7","8","9"];

def corSubFunc(func):
	n=0;
	wordList = getSubFunc(func)[0];
	wordPosList = getSubFunc(func)[1];
	while n < len(wordList):
# Functions
#       Trigonometric:
		if wordList[n] in sinList:
                        print("Interpreting "+wordList[n]+"as sine function (numpy.sin).");
                        wordList[n] = "numpy.sin";
		elif wordList[n] in cosList:
                        print("Interpreting "+wordList[n]+"as cosine function (numpy.cos).");
                        wordList[n] = "numpy.cos";
		elif wordList[n] in tanList:
                        print("Interpreting "+wordList[n]+"as tangent function (numpy.tan).");
                        wordList[n] = "numpy.tan";
		elif wordList[n] in arccosList:
                        print("Interpreting "+wordList[n]+"as inverse cosine function (numpy.arccos).");
                        wordList[n] = "numpy.arccos";
		elif wordList[n] in arcsinList:
                        print("Interpreting "+wordList[n]+"as inverse sine function (numpy.arcsin).");
                        wordList[n] = "numpy.arcsin";
		elif wordList[n] in arctanList:
                        print("Interpreting "+wordList[n]+"as inverse tangent function (numpy.arctan).");
                        wordList[n] = "numpy.arctan";
                elif wordList[n] in cotList:
                        print("Interpreting "+wordList[n]+"as cotangent function (1/numpy.tan).");
                        wordList[n] = "1/numpy.tan";
		elif wordList[n] in cscList:
                        print("Interpreting "+wordList[n]+"as cosecant function (1/numpy.sin).");
                        wordList[n] = "1/numpy.sin";
		elif wordList[n] in secList:
                        print("Interpreting "+wordList[n]+"as secant function (1/numpy.cos).");
                        wordList[n] = "1/numpy.cos";
                elif wordList[n] in arccotList:
                        print("Interpreting "+wordList[n]+"as inverse cotangent function (numpy.arctan(reciprocal()).");
                        wordList[n] = "numpy.arctan(numpy.reciprocal())";
                elif wordList[n] in arccscList:
                        print("Interpreting "+wordList[n]+"as inverse cosecant function (numpy.arcsin(reciprocal()).");
                        wordList[n] = "numpy.arcsin(numpy.reciprocal())";
                elif wordList[n] in arcsecList:
                        print("Interpreting "+wordList[n]+"as inverse secant function (numpy.arccos(reciprocal()).");
                        wordList[n] = "numpy.arccos(numpy.reciprocal())";
#       Hyperbolic:
		elif wordList[n] in coshList:
                        print("Interpreting "+wordList[n]+"as cosine hyperbolicus function (numpy.cosh).");
                        wordList[n] = "numpy.cosh";
		elif wordList[n] in sinhList:
                        print("Interpreting "+wordList[n]+"as sine hyperbolicus function (numpy.sinh).");
                        wordList[n] = "numpy.sinh";
		elif wordList[n] in tanhList:
                        print("Interpreting "+wordList[n]+"as tangent hyperbolicus function (numpy.tanh).");
                        wordList[n] = "numpy.tanh";
                elif wordList[n] in arccoshList:
                        print("Interpreting "+wordList[n]+"as inverse cosine hyperbolicus function (numpy.arccosh).");
                        wordList[n] = "numpy.arccosh";
                elif wordList[n] in arcsinhList:
                        print("Interpreting "+wordList[n]+"as inverse sine hyperbolicus function (numpy.arcsinh).");
                        wordList[n] = "numpy.arcsinh";
                elif wordList[n] in arctanhList:
                        print("Interpreting "+wordList[n]+"as inverse tangent hyperbolicus function (numpy.arctanh).");
                        wordList[n] = "numpy.arctanh";
                elif wordList[n] in cotanhList:
                        print("Interpreting "+wordList[n]+"as cotangent hyperbolicus function (coth).");
                        wordList[n] = "1+(2)/(-1+numpy.exp(2*()))";
                elif wordList[n] in sechList:
                        print("Interpreting "+wordList[n]+"as secant hyperbolicus function (1/numpy.cosh).");
                        wordList[n] = "1/numpy.cosh";
                elif wordList[n] in cschList:
                        print("Interpreting "+wordList[n]+"as cossecant hyperbolicus function (csch).");
                        wordList[n] = "(2*numpy.exp())/(-1+numpy.exp(2*()))";
                elif wordList[n] in arccotanhList:
                        print("Interpreting "+wordList[n]+"as inverse cotangent hyperbolicus function (arccoth).");
                        wordList[n] = "numpy.arctanh(numpy.reciprocal())";
                elif wordList[n] in arcsechList:
                        print("Interpreting "+wordList[n]+"as inverse secant hyperbolicus function (arcsech).");
                        wordList[n] = "numpy.arccosh(numpy.reciprocal())";
                elif wordList[n] in arccschList:
                        print("Interpreting "+wordList[n]+"as inverse cosecant hyperbolicus function (arccsch).");
                        wordList[n] = "numpy.arcsinh(numpy.reciprocal())";
#       Exponents and Logarithms:
                elif wordList[n] in logList:
                        print("Interpreting "+wordList[n]+"as natural logarithm (numpy.log)");
                        wordList[n] = "numpy.log";
		elif wordList[n] in expList:
                        print("Interpreting "+wordList[n]+"as exponential function (numpy.exp)");
                        wordList[n] = "numpy.exp";
#       Misc:
		elif wordList[n] in sgnList:
                        print("Interpreting "+wordList[n]+"as sign function (numpy.sign)");
                        wordList[n] = "numpy.sign";
		elif wordList[n] in absList:
                        print("Interpreting "+wordList[n]+"as absolute value function (numpy.absolute)");
                        wordList[n] = "numpy.absolute";        
		elif wordList[n] in rootList:
                        print("Interpreting "+wordList[n]+"as root function (sqrt)");
                        wordList[n] = "numpy.sqrt";
#                       only square root yet
                elif wordList[n] in minList:
                        print("Interpreting "+wordList[n]+"as minimum value function (numpy.minimum)");
                        wordList[n] = "numpy.minimum";
                elif wordList[n] in maxList:
                        print("Interpreting "+wordList[n]+"as maximun value function (numpy.maximum)");
                        wordList[n] = "numpy.maximum";
                elif wordList[n] in gaussList:
# Constants
                elif wordList[n] in piList:
                        print("Interpreting "+wordList[n]+"as pi ("+scipy.pi+")");
                        wordList[n] = "scipy.pi";
                elif wordList[n] in goldenList:
                        print("Interpreting "+wordList[n]+"as golden ratio ("+scipy.golden+")");
                        wordList[n] = "scipy.golden";
