Title: Python on Static Websites 
Date: 2022-06-24
Category: Python
Tags: pyscript
Slug: Matplotlib Twin Axes 
Author: streetyogi
Summary: Howto create beautiful plots with pyscript and matplotlib


Stil playing around with [PyScript](https://github.com/pyscript/pyscript/blob/main/docs/tutorials/getting-started.md).  
Didn't understand what the fuzz was about, Python in the browser is everywere after all.    
But the fact that you can embed it everywere is huge, no setting up servers, no search for sites that host your Python code, just a static website is enough :)   
Additionally to almost all the modules from the [Python Standard Library](https://docs.python.org/3/library/) you can use over hundred external modules from [Pyodide](https://pyodide.org/en/stable/usage/packages-in-pyodide.html).     
Below is shown a simple graph in [matplotlib](https://matplotlib.org/) that compares treasury bond rates from 2 different years.

 

<html>
    <head>
      <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
      <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" crossorigin="anonymous">
    </head>

  <body>
    <py-env>
      - matplotlib
    </py-env>

    <py-script>
      	import matplotlib.pyplot as plt
	labels = ['1 Mo','3 Mo','6 Mo','1 Yr','2 Yr','3 Yr','5 Yr','7 Yr','10 Yr','20 Yr','30 Yr']
	july16_2007 =[4.75,4.98,5.08,5.01,4.89,4.89,4.95,4.99,5.05,5.21,5.14]
	july16_2020 = [0.12,0.11,0.13,0.14,0.16,0.17,0.28,0.46,0.62,1.09,1.31]
	fig, ax1 = plt.subplots()
	ax1.plot(labels,july16_2007, color='blue', label="july16_2007")
	ax1.set_ylabel("2007", color='blue')
	ax1.spines['left'].set_color('blue')
	ax1.spines['left'].set_linewidth(4)
	for label in ax1.get_yticklabels():
	    label.set_color('blue')
	ax2 = ax1.twinx()
	ax2.plot(labels,july16_2020, color='red', label='july16_2020')
	ax2.set_ylabel("2020", color='red')
	ax2.spines['right'].set_color('red')
	ax2.spines['right'].set_linewidth(4)
	for label in ax2.get_yticklabels():
	    label.set_color('red')
	plt
    </py-script>
  </body>
</html>
