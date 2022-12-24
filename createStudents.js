const { spawn } = require('child_process');

let num = document.getElementById('num').value;

function create(){
    const childPython = spawn('python', ['./creations/createStudents.py', num]);
}
