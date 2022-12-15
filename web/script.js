// async function getDataFromPython() {
//     document.getElementById('test').innerText = await eel.get_data()();
// }

function output(message) {
    document.getElementById('output').innerHTML = "test";
}

document.getElementById('addStudents').addEventListener('click', () => {
    output("test");
    console.log(eel.test());
})