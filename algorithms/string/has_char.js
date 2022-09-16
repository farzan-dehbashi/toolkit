
let string = "here is the string";
let desired_char = "e";
let has_char = false;
if (string.indexOf(desired_char) > -1) {
    has_char = true;
}
console.log(has_char ? "has char" : "has not char");