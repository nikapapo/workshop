    <?php
   
   ini_set('display_errors', 1); //0 to disable
   error_reporting(E_ALL);
   

    $page = isset($_GET['page']) ? $_GET['page'] : 'index'; //echo $page;
    
    //USING VARIABLE INSIDE PHP STRINGS
    // $name = "Nikoloz"; 
    //$using_double_quotes = "My name is $name and I'm here!"; //echo($using_double_quotes);
    //$using_single_quotes = 'My name is '.$name.' and Voila!'; echo $using_single_quotes;
    


    ?>

    <!DOCTYPE html>
    <html>

    <head>
      <meta charset="utf-8">
      <title>Where hardest stuff is possible</title>

      <meta name="viewport" content="width=device-width, initial-scale=1">
      <meta name="description" content="How to use PHP to create a dynamic website">
      <meta name="keywords" content="php,dynamic site,cool,raoul">
      <meta name="author" content="Sorin Paun">

      <link rel="icon" href="img/favicon.png">

      <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto+Slab:400,700|Roboto:300,400">
      <link rel="stylesheet" href="css/style.css">
    </head>

    <body>

      <!-- HEADER -->
      <header class="header">

        <!-- Logo -->
        <figure class="logo-figure">
          <a href="./"><img src="img/logo.svg" alt="The heavy metal company"></a>
        </figure>

        <!-- Nav -->
        <nav class="nav">
          <ul class="menu">
            <li class="menu-item"><a href="?page=index">HOME</a></li>
            <li class="menu-item"><a href="?page=work">WORK</a></li>
            <li class="menu-item"><a href="?page=contact">CONTACT</a></li>
          </ul>
        </nav>

      </header>


      <!-- CONTENT -->
      <main class="content">
  
      <?php 
      //grab an external content
     // include ("html/index.html");
      //include once
      //include ("html/index.html");
      
      //require function
      //require("html/index.html");
      //require once function
      require_once("html/$page.html");

      ?>
        

      </main>


    <!-- FOOTER -->
    <footer class="footer">
      <p>&copy;1998 - 2019 - Heavy Metal Company</p>
    </footer>

  </body>

  </html>