function option(a,b,c,d,e,f){
    document.getElementById('line').style.transform="translateX("+a+"px)";
    document.getElementById('line').style.width=f+"px";
    document.getElementById(b).style.display="block";
    document.getElementById(c).style.display="none";
    d.style.color="black";
    document.getElementById(e).style.color="grey";

}
function nav(a,b,c){
    var op=["h","u","a","l"];
    

    for(let i=0;i<=op.length-1;i++){
        document.getElementById(op[i]).style.backgroundColor="white";
    }
    a.style.backgroundColor="rgba(0,0,250,0.1)";
    document.getElementById(b).style.display="block";
    document.getElementById(c).style.display="none"


}
function prev(a){
    document.getElementById("prev").style.display="flex";
    var ur=document.getElementById("image").value;
    document.getElementById("im").src=String(ur)
}
function fet(){
    fetch("http://127.0.0.1:8000/process")
  .then((response) => response.json())
  .then((json) => {console.log(json);
  if(json.status=="ok"){
    fetch("http://127.0.0.1:8000/result")
  .then((response) => response.json())
  .then((json) => {
    var d=JSON.parse(json);

    console.log(d)
})
}
else{console.log("error")}});

}