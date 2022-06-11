function ranklist(input){
    let count = Number(input[0]);
    let startingPoints = Number(input[1]);
    let inputL = input.length;
    let pointsMatch = 0;
    let averagePerMatch = 0;
    let wCount = 0;
    let averagePercent = 0;
    for(let i=2; i<inputL; i++){
        let situation = input[i];
        if(situation === "F"){
            startingPoints += 1200;
            pointsMatch += 1200;
        }
        else if(situation === "W"){
            startingPoints += 2000;
            pointsMatch += 2000;
            wCount += 1
        }
        else if(situation === "SF"){
            startingPoints += 720;
            pointsMatch += 720;
        }
    }
    averagePerMatch = pointsMatch / count
    averagePercent = (wCount / count) * 100
    console.log(`Final points: ${Math.floor(startingPoints)}`)
    console.log(`Average points: ${Math.floor(averagePerMatch)}`)
    console.log(`${averagePercent.toFixed(2)}%`)
}
ranklist(["4",
"750",
"SF",
"W",
"SF",
"W"])
;
