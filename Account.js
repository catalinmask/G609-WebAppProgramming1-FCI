var diferenta=0;
var f='';
function Account(){
    fetch("http://localhost:3004/api/v1/Account", {headers:{"Authorization":"Bearer "+sessionStorage.token}})
        .then(date => date.json())
        .then(data =>{ console.log(data)
          const a=document.getElementById("MailAccount");
          const b=document.getElementById("UsernameAccount");
          const c=document.getElementById("MarcaMasinaAccount");
          const d=document.getElementById("KmMasinaAccount");
          const e=document.getElementById("KmSchimbAccount");
          a.innerText=data["email"];
          b.innerText=data["username"];
          c.innerText=data["marca_masina"];
          d.innerText=data["km_masina"];
          e.innerText=data["km_schimb"];
          diferenta =data["km_schimb"]-data["km_masina"];
        })
}

function Calculeaza(){
  var KmPeZi=document.getElementById("KmPeZi").value;
  const dataSchimb=diferenta/KmPeZi;
  console.log(KmPeZi);
  console.log(diferenta);
  console.log(dataSchimb);
  f=document.getElementById("Data");
  f.innerText=dataSchimb;
}

