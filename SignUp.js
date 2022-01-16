const LoginPageUrl="/Users/catalinflorea/Desktop/ProiectFinal/login.html"
function parola() {
  var pw1 = document.getElementById("Password");
  var pw2 = document.getElementById("secondPassword");
  if (pw1.type === "password" && pw2.type === "password") {
    pw1.type = "text";
    pw2.type = "text";
  } else {
    pw1.type = "password";
    pw2.type = "password";
  }
}

function sendData() {
  const a = document.getElementsByName("Email")[0].value;
  const b = document.getElementsByName("Username")[0].value;
  const c = document.getElementsByName("Password")[0].value;
  const d = document.getElementsByName("secondPassword")[0].value;
  const e = document.getElementsByName("MarcaMasina")[0].value;
  const f = document.getElementsByName("KmMasina")[0].value;
  const g = document.getElementsByName("KmSchimb")[0].value;
  const body = {
    email: a,
    username: b,
    Password: c,
    secondPassword: d,
    marca_masina: e,
    km_masina: f,
    km_schimb: g,
  };
  const option = {
    method: "POST",
    mode: "cors",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(body),
  };
  fetch("http://localhost:3004/api/v1/signUp", option)
    .then(showSuccess)
    .then(Success, Failure)
    .catch(showError);
}
function showSuccess(response) {
  if(!response.ok){
     throw response; //throw error
  }
  return response;
}
function Success(response){
  window.location.href = LoginPageUrl;
}
function Failure(response){
  return response.JSON().then(showError); 
}

function showError(response) {
  console.log(JSON.stringify(response));
  const body=document.getElementsByTagName("body")[0];
  const errorDiv=document.createElement("div");
  const errorPar=document.createElement("p");
  errorPar.innerText=response.error;
  errorDiv.appendChild(errorPar);
  body.appendChild(errorDiv);
}

function btnCancel2() {
  document.getElementById("Mail").value='';
  document.getElementById("Username").value='';
  document.getElementById("Password").value='';
  document.getElementById("secondPassword").value='';
  document.getElementById("MarcaMasina").value='';
  document.getElementById("KmMasina").value='';
  document.getElementById("KmSchimb").value='';
}

