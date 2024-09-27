function translate() {
    fetch("/translate").then(resp=>{
        resp.json().then(result=>{
            result["translated"]
        })
    }).catch(console.log);
}

alert();