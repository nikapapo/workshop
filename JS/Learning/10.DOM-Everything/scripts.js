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


// Target element → classic approach
const main = document.querySelector('main');


// Target element → awesome approach
//const main = $('main');
//console.log(main);


// Manage attribute

$('h1').setAttribute('id','main-title');
$('p').setAttribute('class','row');
$('#p4').removeAttribute('class');

//* MANAGE CLASSE ATTRIBUTE */
$ ('body').classList.add('menu-is-open');
$ ('body').classList.remove('menu-is-open');



// →→→ CREATE ELEMENT [Classic approach]
const p1 = document.createElement('p');//make..//

p1.setAttribute('class','row');
p1.innerHTML = "Je suis le texte du nouveau parahraphe!" 
$('main').append(p1);

const span = make('span',);
span.textContent = " Info: ";
p1.prepend(span);

//*REMOVE ELEMENT-----
//$('Html').remove();


// →→→ ADD TEXT CONTENT
p1.textContent = 'A simple text.';



// →→→ ADD HTML CONTENT
//p1.innerHTML = '<span class="success"> Info: </span> A comlex content >


//*CHALLENGE

let div1 = make('div');
let div2 = make('div'); 

div1.setAttribute('id','adm-msg');
div1.setAttribute('class','message');
div2.setAttribute('class','message');

div2.innerHTML = "blablabla"

div1.prepend(div2);
 $('body').insertBefore(div1, $('script'));
//$('body').append(div1);









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



