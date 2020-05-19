let todos =  {


    /* TODO LIST
    ------------------ */
     todoList : [
      "Go Shoping",
      "By Tobacco",
      "Do this",
      "Do that"

    ],

    


/*DISPLAY TODOS
-----------------------------*/
displayTodos :function () {

  console.log(this.todoList);
},

/* ADD TODO
----------------------*/

addTods : function(text) {

  this.todoList.push(text);
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

todos.displayTodos();
todos.addTodo("Test");
todos.deleteTodo(1,"Test");
todos.deleteTodo(2, "Some other value");











/* ADD TODO
----------------------*/

function addTodo(text) {

}




