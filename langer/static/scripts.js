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
        body: jsonStr(data)
    }).then(resp=>{
        resp.text().then(result=>{
            let translated = result["translated"];
            console.log(result)
            output.value = result["translated"];
        })
    }) // .catch(console.log);
}

function readSettings() {
    let settings = {};
    settings["from"] = fromLang.value;
    settings["to"] = toLang.value;
    settings["dificulty"] = dificulty.value;
    
    localStorage.langSettings = jsonStr(settings);
    
}

function readAloud() {
    let text = translated.textContent,
    lang = {"French": "fr-FR", "Spanish": "es-ES"}[to.value],
    voices = speechSynthesis.getVoices();
}

addEventListener("click", (event)=>{
    switch (event.target.id) {
        case "translate":
            console.log(write.value, from.value, to.value, translated);
            return;
            translate(write.value, from.value, to.value, translated);
            break;

        case "SETTINGS":
            event.preventDefault();
            readSettings();
            location.href = "/game"
            break;
    
        default:
            break;
    }
});