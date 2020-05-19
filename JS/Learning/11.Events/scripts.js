// →→→ HELPER FUNCTION → TARGET ANY SELECTOR
function $(selector) {
  return document.querySelector(selector)
}

function $$(selector) {
  return document.querySelectorAll(selector);
}



// →→→ HELPER FUNCTION → CREATE ANY ELEMENT
function make(selector) {
  return document.createElement(selector);
}

let div1 = make('div');
let div2 = make('div'); 

div1.setAttribute('id','adm-msg');
div1.setAttribute('class','message');
div2.setAttribute('class','message');

div2.innerHTML = "blablabla"

div1.prepend(div2);
 
//$('body').insertBefore(div1, $('script'));
//$('body').append(div1);

//**EVENTS */

/*The even listener need two arguments:
the event and the action*/
let count = 0;


$('#btn1').addEventListener('click',function(){ 
  count++;
  $('#msg').innerHTML += "I JUST CLICKED ! ";
  $('#p1').innerHTML = count;
});


// →→→ YOU CAN DO MORE WITH HTML CONTENT
// insertAdjacentHTML()
// The four positions available are:
// "beforebegin" (directly before the current node)
// "afterbegin" (inside the current node, at the beginning)
// "beforeend" (inside the current node, at the end)
// "afterend" (directly after the current node)


// This will only touch the first item of his kind


// This will touch all of them
//$$('p').forEach(function(item){ 
//item.style.color = '#ccc';});


// →→→ DO STYLES
$('#p2').style.color = '#f00';
$('#p3').style.backgroundColor = '#ccc';
$('#p4').style.cssText = 'background-color : #fc0';

// →→→ INSERT, APPEND, PREPEND



