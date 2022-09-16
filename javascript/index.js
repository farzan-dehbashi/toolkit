function createCircle(){
    return {
        radius: 1,
        location: {
            x:0, y:1
        },
        isVisible: true,
        draw: function(){
            console.log('draw');
        }
    
    }
}