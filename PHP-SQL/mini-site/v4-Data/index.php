    <?php
   
   ini_set('display_errors', 1); //0 to disable
   error_reporting(E_ALL);
   
  //my custom print_r function
   function show($arr){
    
    echo '<pre>';
    print_r($arr);
    echo '</pre>';
}
    // get page from URI
    $page = isset($_GET['page']) ? $_GET['page'] : 'index'; //echo $page;
    //Grab THE JSON CONTENT
    $site_data_json = file_get_contents("site_data.json");
    //CONVERT THE JSON CONTENT INTO PHP ARRAY
    $site_data = json_decode ($site_data_json,true);
    //hes two arguments: the json string and data tupe  
    //if tru convrtion to array
    //if false --> conversion to an object (by default)
   
    $pages = $site_data['pages'];
    //show($pages['work']['title'] );

      
    ?>

    <!DOCTYPE html>
    <html>

    <head>
      <meta charset="utf-8">
      <title><?php echo $pages[$page]['title'] ;?></title>

      <meta name="viewport" content="width=device-width, initial-scale=1">
      <meta name="description" content="<?php echo $site_data['description'];?>">
      <meta name="keywords" content="<?php echo $site_data['keywords'];?>">
      <meta name="author" content="<?php echo $site_data['author'];?>">

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
      <!--MAIN TITLE-->
      <h1 class="main-title"><?php echo $pages[$page]['title'] ;?></h1>


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