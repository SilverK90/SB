function Get() {
    var name = document.getElementById('name').value;
    var age = (document.getElementById('age').value).toInt();
    document.getElementById('result').innerHTML = typeof age;
}