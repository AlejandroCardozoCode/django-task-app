// botones
const btnDeleteTask = document.querySelector(".btn-task--delete");
const btnDoneTask = document.querySelector(".btn-task--done");
const taskListContainer = document.querySelector(".task-list");
const taskContainer = document.querySelector(".task-container");
const taskModal = new bootstrap.Modal(document.getElementById('taskModal'));

taskListContainer.addEventListener("click", taskStateHandler)

function getCSRFToken() {
    const cookieValue = document.cookie.match(/csrftoken=([^;]+)/);
    return cookieValue ? cookieValue[1] : null;
}

async function taskStateHandler(event) {
    if (event.target.classList.contains("btn-task--delete")) {
        const taskId = event.target.closest("li").dataset.taskId;
        const response = await fetch(`/delete_task/${taskId}`,
            {
                method: "DELETE",
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken() // Incluir el token CSRF en el encabezado
                }
            });
        if (response.ok) {
            location.reload();
        }
        else {
            alert(`No se ha podido procesar la solicitud ${response.status}`)
        }
    }

    else if (event.target.classList.contains("btn-task--done")) {
        const taskId = event.target.closest("li").dataset.taskId;
        const response = await fetch(`/done_task/${taskId}`,
            {
                method: "PUT",
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken() // Incluir el token CSRF en el encabezado
                }
            });
        if (response.ok) {
            location.reload();
        }
        else {
            alert(`No se ha podido procesar la solicitud ${response.status}`)
        }

    }

    // actualizar valores de cada tarea
    const taskId = event.target.closest("li").dataset.taskId;
    const response = await fetch(`/task/${taskId}`)
    const data = await response.json()
    taskModal.show()
    document.getElementById("taskModalTitle").innerHTML = data.title;
    document.getElementById("taskModalDescription").innerHTML = data.description;

}
