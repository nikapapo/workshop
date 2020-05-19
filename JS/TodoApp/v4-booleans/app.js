let todos =  {


    /* TODO LIST
    ------------------ */
     todoList: [

    {text: "Go shopping",completed :false},
    
    {text: "Buy Tobacco",completed :false},
    
    {text: "Do this",completed :false},
    
    {text: "Do that",completed :false}
    ],

    


/*DISPLAY TODOS
-----------------------------*/
displayTodos :function () {

  //console.log(this.todoList);
},

/* ADD TODO
----------------------*/

addTods : function(newText, newcompleted= false) {

    this.todoList.push( {
      text : newText,
      completed :newcompleted
    });                                  
     this.displayTodos();
  },
  

/*CHANGE TODO
-----------------------------------*/
changeTodo :function(index, text){

 
},


/* DELETE A TODO
-------------------------------------------*/

deleteTodo : function(index, numberToDelete) {
}

}












/* ADD TODO
----------------------*/

function addTodo(text) {

}



todos.todoList[0];
//console.log(todos.todoList[0].text );
//console.log(todos.todoList[0].completed );



/*----------Practice----
------------------- */

let myList = [
     {
    text: "learn JS",
    deadline: "31.04.20",
    completed: true
  },
  
  {
    text: "learn Css",
    deadline: "31.04.20",
    completed: false
  },
  
  {
    text: "learn HTML",
    deadline: "31.04.20",
    completed: false
  },

  {
    text: "learn PHP",
    deadline: "31.04.20",
    completed: true
  },
   
   

];
    
   //Show (myList[0]["deadline"]);//square braqets
   //Show (myList[0].deadline);

   myList[1].completed = true;
   //show(myList[1]);
   
   myList.splice(1,1);
   //show(myList);

   myList.push({
    text: "learn All staf",
    deadline: "31.04.20",
    completed: true
  },);
  //show(myList);
  
  
  function addItem (newtext,newdeadline, newcomplated = false)
  { 
    myList.push({
      text : newtext,
      deadline : newdeadline,
      complated : newcomplated


    }
    );
     

  }
  //addItem("learn Javascript"," 06.06.20")
  //show(myList);


   function deleteItem (index, deletn=1){
     
    myList.splice (index, deletn);
   }
   //deleteItem(1, myList.length);//deletes everything after spacyfied item

  //show(myList);


  function changeKeyValue (index, key, value)
  {
   myList[index][key] = value;


  }
    changeKeyValue(1, "complated", true);
    show(myList);




