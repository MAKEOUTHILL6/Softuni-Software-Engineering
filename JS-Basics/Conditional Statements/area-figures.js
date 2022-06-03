function area(input){
    let figure = input[0];
    let sideOne = Number(input[1]);
    let sideTwo = Number(input[2]);
    let area = 0;

    if(figure === "square"){
        area += Math.pow(sideOne, 2);
    }
    else if(figure === "rectangle"){
        area += sideOne * sideTwo;
    }
    else if(figure ===  "circle"){
        area += Math.PI * Math.pow(sideOne, 2);
    }
    else if(figure === "triangle"){
        area += (sideOne * sideTwo) / 2
    }
    console.log(area.toFixed(3));
}
area(["circle",
"6"])
