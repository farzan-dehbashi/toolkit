function Circle (attr1){
    this.attr1 = attr1;
    this.method = function() {
        console.log("this is a method")
    }
}

var circle = new Circle(1)

