const { spawn } = require('child_process');

// template for calling python functions( note: when testing the function has to be right under the spawn variable)



// const createAssignments = spawn('python', ['./creations/createAssignment.py', "Assignment name", "subject", "grade"])
// const createEvents = spawn('python', ['./creations/createEvent.py', "sport", "grade"]);
const createStudents = spawn('python', ['./creations/createStudents.py',4]);