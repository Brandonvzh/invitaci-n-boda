document.getElementById("input-invitados").style.display = 'none';
document.getElementById("input-asistentes").style.display = 'none';
document.getElementById("idInput").style.display = 'none';

function myFunction() {
    const code = document.getElementById('code').value;
  
    console.log(code)
    // Hacer consulta de datos en API:
    getData(code);
}

const getData = async (code) => {
    try {
        

        const currentURL = new URL(window.location.href);
        const apiURL = currentURL.origin + "/api/v1/guests/" + code + "/";

        const response=await fetch(apiURL);
        // console.log(response);

        const data = await response.json();
        console.log(data);

        document.getElementById("code").style.display = 'none';
        document.getElementById("code_submit").style.display = 'none';
        document.getElementById("labelInvitacion").style.display = 'none';
        document.getElementById("no-codigo").style.display = 'none';
        document.getElementById("intento").style.display = 'none';

        document.getElementById("label-asistencia").style.display = "flex";
        document.getElementById("select-asistencia").style.display = "flex";

        document.getElementById("invitados").textContent = `Hola, ${data[0]["identifier"]}`;
        document.getElementById("asistentes").textContent = `Se asignaron: ${data[0]['num_guests_assigned']} invitados`;
        document.getElementById("idInput").value = data[0]['id'];
        // console.log(data);
        // console.log(data[0]['code']);
        // console.log(data[0]['num_guests_assigned']);
        // console.log(data[0]['identifier']);
    } catch (error) {
        document.getElementById("intento").style.display = 'flex';
        document.getElementById("no-codigo").style.display = 'flex';
        document.getElementById("no-codigo").textContent = `No se encontró registro del código.`;
        document.getElementById("intento").textContent = `Volver a escribir código:`;
        document.getElementById("label-asistencia").style.display = "none";
        document.getElementById("select-asistencia").style.display = "none";
        document.getElementById("code").value = "";
        document.getElementById("code").style.display = "flex"; 
        document.getElementById("code_submit").style.display = 'flex';
    }
}

function mostrarCampos() {
    var seleccion = document.getElementById("select-asistencia").value;

        if (seleccion === "Sí asistiré") {
            document.getElementById("input-invitados").style.display = "flex";
            document.getElementById("input-asistentes").style.display = "flex";
            document.getElementById("button-registrar").style.display = "flex";
            document.getElementById("label-asistencia").style.display = "none";
            document.getElementById("select-asistencia").style.display = "none";
        }

        if (seleccion === "No asistiré") {
            document.getElementById("label-asistencia").style.display = "none";
            document.getElementById("select-asistencia").style.display = "none";
            document.getElementById("label-noasistencia").style.display = "flex";

            document.getElementById("input-invitados").value = "0";
            document.getElementById("input-asistentes").value =  "No se asistirá";

            document.getElementById("button-registrar").style.display = "flex";
        }
}