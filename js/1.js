async function get_Local() {
    let response = await fetch("http://localhost:8000/api/Local/all");
    if (response.ok) {
        let json = await response.json();
        return json;
    } else {
        alert("Ошибка HTTP: " + response.status);
    }
}

async function render_Local() {
    let template = `
    <h2>Название новости = {НАЗВАНИЕ}</h2>
    <p>{ОПИСАНИЕ}</p>
    <img src = "{КАРТИНКА}">
    `;

    let Locals = await get_Local();
    let container = document.getElementById("Local");
    Locals.forEach(element => {
        let Local = template
            .replace("{НАЗВАНИЕ}", element.Name)
            .replace("{ОПИСАНИЕ}", element.descrtiption)
            .replace("{КАРТИНКА}", element.picture)
        container.innerHTML += Local;
    });
}

render_Local();
