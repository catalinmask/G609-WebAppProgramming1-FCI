const AccountPageUrl="/Users/catalinflorea/Desktop/ProiectFinal/Account.html"
function ShowSuccess(response){
    if(!response.ok){
        throw response;// arunc raspunsul sub forma de eroare
    }
    return response;
}

function Success(response){
    window.location.href = AccountPageUrl;
}

function Failure(response){
    return response.JSON().then(error);
}

function showError(response){
    let errorPar=document.getElementsByName("errorParagraph")[0];
    if(!errorPar){
        const body=document.getElementsByTagName("body")[0];
        const errorDiv=document.createElement("div");
        errorPar=document.createElement("p");
        errorPar.innerText=response.error;
        errorPar.setAttribute("name", "errorParagraph");
        errorDiv.appendChild(errorPar);
        body.appendChild(errorDiv);

    }else{
        errorPar.innerText=response.error;
    }
}

function Login(){
    const body={
        "username": document.getElementsByName("UsernameLogin")[0].value,
        "password": document.getElementsByName("PasswordLogin")[0].value,
    }
    const params={
        method: "POST",
        mode: "cors",
        headers:{
            "Content-Type": "application/json"
        },
        body: JSON.stringify(body)
    };
    fetch("http://localhost:3004/api/v1/signIn",params)
        .then(ShowSuccess)
        .then(Success, Failure)
        .catch(showError)
} 
