const circle = {
    radios: 1,
    location: {
        x: 1,
        y:2
    },
    isVisible: true,
    draw: function(){
        console.log("hi");
    }
}

function createCircle(radius){
    return {
        radius,
        draw(){
            console.log("draw");
        }
    }
}

const circle1 = createCircle(1);
console.log(circle1)