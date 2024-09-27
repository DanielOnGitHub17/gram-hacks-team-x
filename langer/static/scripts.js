identify();

function translate(text, from, to, output) {
    let data = {};
    data["text"] = text;
    data["from"] = from;
    data["to"] = to;
    fetch("/translate", {
        headers: {
            "Content-Type": "application/json",
        },
        method: "POST",
        body: data
    }).then(resp=>{
        resp.text().then(result=>{
            let translated = result["translated"];
            console.log(result)
            output.textCountent = result["translated"];
        })
    }) // .catch(console.log);
}

addEventListener("click", (event)=>{
    console.log(event.target.id);
    switch (event.target.id) {
        case "TRANS":
            translate(TEXTBOX.value, "english", "spanish", DISPLAY)
            break;
    
        default:
            break;
    }
});