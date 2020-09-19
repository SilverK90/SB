function Get() {
    var name = document.getElementById('name').value
    var age = document.getElementById('age').value
    var Fromdate = document.getElementById('Fdate').value
    var Todate = document.getElementById('Tdate').value
    // document.getElementById('name_output').innerHTML = "Name : " + name
    // document.getElementById('age_output').innerHTML = "Age : " + age
    // document.getElementById('fdate_output').innerHTML = "From : " + Fromdate
    // document.getElementById('tdate_output').innerHTML = "To : " + Todate
    eel.GetResult(name, age)(got_from_python)
}
function got_from_python(result){
    for(x of result){
        var pEle = document.createElement("P")
        pEle.innerHTML = " "+x
        document.body.appendChild(pEle)
    }
    
}
// eel.expose(SetData);
// function SetData(output){
//     document.getElementById('name_output').innerHTML = output
// }