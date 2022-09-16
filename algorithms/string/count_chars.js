let string = "here is the string here is thisg";
let dict = {};

for (i = 0; i < string.length; i++) {
    let char = string[i];
    if (char in dict){
        dict[char] = dict[char] + 1;
    }
    else {
        dict[char] = 1;
    }
}

console.log(dict);