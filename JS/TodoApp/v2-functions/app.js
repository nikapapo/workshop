/* TODO LIST
------------------ */
let todoList = [
  "Go Shoping",
  "By Tobacco",
  "Do this",
  "Do that"

];

/*DISPLAY TODOS
-----------------------------*/
function displayTodos() {


  console.log(todoList);
}
displayTodos();



/* ADD TODO
----------------------*/

function addTodo(text) {

todoList.push("text");
displayTodos();

}
addTodo("Me new Todo");

/*CHANGE TODO
-----------------------------------*/
function changeTodo(index, text) {

  todoList[index] = text;
  displayTodos();
  
}
changeTodo(1, "buy cars");

/* DELETE A TODO
-------------------------------------------*/

function deleteTodo(index, numberToDelete) {

  todoList.splice(index, numberToDelete);
  displayTodos();

}

deleteTodo(2, 2);

