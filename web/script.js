function log(message) {
    logs = document.getElementById("log");
    logs.value += message + "\n";
    console.log(message)
}

function addStudents(num) {
    eel.createStudents(num)
}

function reset() {
    eel.createWorkers()
}

function createEvent(eventName, grade) {
    console.log("test")
    eel.createEvent(grade)
}

function assignmentCreation(assignmentName, grade) {
    let radioButtons = document.querySelectorAll('input[name="type"]');
    let selectedValue;
    for (let i = 0; i < radioButtons.length; i++) {
        if (radioButtons[i].checked) {
            selectedValue = radioButtons[i].value;
            eel.assignmentCreation(assignmentName, selectedValue, grade)
            log("The assignment named, " + assignmentName + "was posted and graded!")
            break;
        }
    }
}
