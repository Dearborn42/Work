async function getDataFromPython() {
    document.getElementById('test').innerText = await eel.get_data()();
}

document.getElementById('').addEventListener('click', () => {
    console.log(getDataFromPython())
})