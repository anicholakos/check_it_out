<!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="utf-8">
      <title>{{title}}</title>
      <style type="text/css">
        @import url(/static/css/global.css);
	/*
	    CSS written by Aki Nicholakos and Alex Hirschberg
	*/
	body
	{
	    background-color:#D8D8D1;
	    /*background-image:url("http://i.imgur.com/tTsKPob.png");
	    background-size:50%;*/
	}
	table, td, th
	{
	    border:2px solid #002900;
	    border-collapse:collapse;
	    padding:10px;
	    background-color:white;
	}
	table
	{
	    margin:20px;
	}
	th 
	{
	    background-color:#FF9900;
	}
	td
	{
	    font-size:110%
	}
      </style>
    </head>
  <body>
    <nav>
      <ul>
        <li><a href="/persons">People</a></li>
        <li><a href="/loans">Loans</a></li>
        <li><a href="/items">Items</a></li>
      <ul>
    </nav>
    <section>
      %include
    </section>
  </body>
</html>
