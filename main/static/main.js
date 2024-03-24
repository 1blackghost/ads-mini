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
let i,j;
    const bad=json["true"];
    const good=json["false"];

    for(i=0;i<=bad.length-1;i++){
        document.getElementById("list").innerHTML+="<div class='bad'>
                        <p>"+bad[i]+"</p>
                        <img src='/static/images/bad.jpg'/>
                    </div>"
    }
      for(i=0;i<=good.length-1;i++){
        document.getElementById("list").innerHTML+="<div class='good'>
                         <p>"+good[i]+"</p>
                        <img src='/static/images/good.jpg'/>
                    </div>"
      }
})
}
else{console.log("error")}});

}
