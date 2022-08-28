function ch(){
        checkpass()
        num()}


function checkpass(){
var password = document.getElementById("password")
  , confirm_password = document.getElementById("confirm_password");
  if(password.value != confirm_password.value) {
    confirm_password.setCustomValidity("Passwords Don't Match");
  } else {
    confirm_password.setCustomValidity('');
  }
}
password.onchange = checkpass();
confirm_password.onkeyup = checkpass();

function num(){
var ph = document.getElementById("phonenum");
  if(ph.value.length==10)
  {
    phonenum.setCustomValidity('');
  } else {
    phonenum.setCustomValidity("enter valid mobile number");
  }
}
