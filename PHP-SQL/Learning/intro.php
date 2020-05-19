<?php
/*COMENTS */
// single line coment
/* MULTI LINE 
COMMENT */
# ALSO SINGLE LINE COMMENT

/* VARIABLES USE $ SINGN
-------------------------*/

$num = 4;
$str = "String";
$bool = true;
$arr = [1,2,3,4];
$void =null;


/*ARRAYS
 --------------------*/

 $arr = [1,2,3,"String",0,null];// like in JS
 $arr = array(1,2,3,"string",false,null); 
 //echo $arr[3];// shows 3rd index;
 //print $arr[3];//idem
 //var_dump($arr);

 array_push ($arr,"bob");
 array_pop($arr);
 //show ($arr);
 array_shift($arr);
 //show ($arr);
// var_dump($arr);

 //show ($arr);
//PUSHING SOMETHING AT THE END
 $arr [] = "Something at the end...";
 $arr[2] = 33;

 
 show ($arr);


 // MULTIDIMENSIONAL ARRAY
$website_data = [
     'global-title' => "This is my firts PHP website",
     'keywords'     => "php,dev,bob",
     'author'       => "Nikoloz",
     'pages'        => [
        
          'home'      => [
          
          'title'    => "Welcome to my humble abode",
          'menu'     => "Home"
          ]
     ],
     
  
    ];

$pages = $website_data ['pages'];
 //show($website_data['pages');

// A FUNCTION USES LOCAL SCOPE
// I HAVE TO USE A SPECIAL KEYWORD
//IN ORDER TO USE GLOBAL SCOPO

/*LOOPS-----
----------------------- */

 $n = 10;

 
 for ($i = 1; $i <= $n; $i++){

     show($i); 
}

//BEST FOR ARRAY IS TO USE FOREACH() LOOP

// A FOREACH COULD RETUR ONLY VALUES OR
// THE PAIR KEY/VALUE
foreach($website_data as $key => $val) {
     show($val);
}




 /* FUNCTIONS------
 ----------------------------- */

 function show($arr){

      echo '<pre>';
      print_r($arr);
      echo '</pre>';
 }

function calculate_surface($width, $lenght){
     
    // echo $width * $lenght;

     
     return $width * $lenght;
}
 $calc = calculate_surface(24,24);
 //show($calc);
