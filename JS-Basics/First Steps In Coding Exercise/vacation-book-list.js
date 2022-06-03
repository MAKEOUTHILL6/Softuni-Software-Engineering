function read(input){
    let pages = Number(input[0]);
    let pagesPerHour = Number(input[1]);
    let days = Number(input[2]);
    let totalTime = pages / pagesPerHour;
    let neededTime = totalTime / days;
    console.log(neededTime);
}
read(["212 ",
"20 ",
"2 "]
)