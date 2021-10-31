from flask import Flask, request, render_template
#import numpy as np
app = Flask(__name__)
#app.config["DEBUG"] = True

words = open("usa2.txt", 'r').readlines()
words=[word[:-1] for word in words]

#dp = np.zeros(shape=(50, 50))
dp = [[0 for x in range(25)] for y in range(25)] # for some reason non np array is faster

def ed(a, b):
	c = len(a) + 1
	r = len(b) + 1
	for i in range(1, r):
		dp[i][0]=i
	for i in range(1, c):
		dp[0][i]=i
	for i in range(1, r):
		for j in range(1, c):
			dp[i][j]=0
			if a[j-1]!=b[i-1]:
				dp[i][j]=min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])+1
			else:
				dp[i][j]=dp[i-1][j-1]
	return dp[r-1][c-1]

def compute(s):
	l=[]
	for word in words:
		l.append([word, ed(word, s)])
	l.sort(key=lambda x: x[1])
	ans=""
	for i in ([item[0] for item in l[:50]]):
		ans+=i+", "
	return ans+"..."

#@app.route('/')
#def index():
#	return render_template('index.html')

@app.route('/', methods=["GET", "POST"])
def adder_page():
	if request.method == "POST":
		print("here")
		s = str(request.form["s"])
		result=compute(s)
		return '''
			<html>
				<body>
					<p>do you  mean {result}</p>
					<p><a href="/">try again?</a>
				</body>
			</html>
		'''.format(result=result)
	elif request.method=="GET":
		return render_template('index.html')

if __name__ == '__main__':
	app.run()
