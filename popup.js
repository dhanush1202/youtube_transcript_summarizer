const btn=document.getElementById("summarize");
btn.addEventListener("click",function(){
    btn.disabled=true;
    btn.innerHTML="summarizing...";
    chrome.tabs.query({currentWindow: true,active:true},function(tabs){
        var url=tabs[0].url;
        var x=new XMLHttpRequest();
        x.open("GET","http://127.0.0.1:5000/summary?url="+url,true);
        x.onload=function(){
            var text=x.responseText;
            const p=document.getElementById("output");
            p.innerHTML=text;
            btn.disabled=false;
            btn.innerHTML="summarize";
        }
        x.send();
    })
})
