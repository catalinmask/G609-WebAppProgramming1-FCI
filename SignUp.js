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

function btnCancel2() {
  const intrebare = document.createElement("div");
  intrebare.innerHTML =
    "Warning! Your are about to reset your inputs. Are you sure you want to continue?";
  intrebare.style.fontSize = "20px";
  intrebare.style.color = "red";
  intrebare.style.position = "relative";
  intrebare.style.textAlign = "center";

  document.getElementById("divMare").appendChild(intrebare);
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
    .then(showSuccess())
    .catch(showError(body));
}
function showSuccess() {
  alert("Te-ai inregistrat cu success!");
}
function showError(r) {
  console.log(JSON.stringify(r));
}
