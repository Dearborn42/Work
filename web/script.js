function log(message) {
    logs = document.getElementById("log");
    logs.value += message + "\n";
}

function reset() {
    eel.createWorkers()
    log("Reset")
}

function createEvent(grade) {
    let event = document.getElementById('eGrade').value;
    log(event + " event was created")
    eel.createEvent(grade)
}

function assignmentCreation(assignmentName, grade) {
    let radioButtons = document.querySelectorAll('input[name="type"]');
    let selectedValue;
    for (let i = 0; i < radioButtons.length; i++) {
        if (radioButtons[i].checked) {
            selectedValue = radioButtons[i].value;
            eel.assignmentCreation(assignmentName, selectedValue, grade)
            log("The assignment named, " + assignmentName + " was posted and graded!")
            break;
        }
    }
}

function addStudents(num) {
    eel.createStudents(num)
    log(`Added ${toString(num)}Students.`)
}
