function area(input){
    let length = Number(input[0]);
    let width = Number(input[1]);
    let height = Number(input[2]);
    let percent = Number(input[3]);
    let total = length * width * height;
    let totalLit = total / 1000;
    let takenSpace = percent / 100;
    let neededLit = totalLit * (1 - (1 * takenSpace));
    console.log(neededLit);
}
area(["85 ",
"75 ",
"47 ",
"17 "]
);