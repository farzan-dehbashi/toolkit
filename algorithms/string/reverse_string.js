let string = "abc";
for (var i = 0; i < string.length; i++) {
    console.log(string);
    console.log(string[i]);
    let temp = string[i];
    string.replace(i, string[string.length - 1 - i]);
    string.replace(string.length - 1 - i, temp);
    console.log(string[string.length - 1 - i]);
}
console.log(string);