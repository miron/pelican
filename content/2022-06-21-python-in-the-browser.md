---
Title: "Python in the Browser"
date: 2022-06-21
---

Python code embedded in html which samples random Austrian lottery numbers.  
Also prints the date and writes into labeled elements.  
Bear in mind that this is just a simple static website :)  
Uses [PyScript](https://github.com/pyscript/pyscript/blob/main/docs/tutorials/getting-started.md). Check it out for some examples.  

<html>
    <head>
      <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
      <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" crossorigin="anonymous">
    </head>

  <body>
    <b><p>Today is <u><label id='today'></label></u></p></b>
    <br>
    <div id="lotto" class="alert alert-primary"></div>
    <py-script>
      import datetime as dt
      from random import sample
      pyscript.write('today', dt.date.today().strftime('%A %B %d, %Y'))
      pyscript.write('lotto', f'{sample(range(1,46), 6)}')
    </py-script>
  </body>
</html>
