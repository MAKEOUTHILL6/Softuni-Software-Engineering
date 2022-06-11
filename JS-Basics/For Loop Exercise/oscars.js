function oscars(input){
    let actorName = input[0];
    let academyPoints = Number(input[1]);
    let sumPoints = 0;
    let inputL = input.length;
    for(let i=3; i<inputL; i++){
        if(i % 2 !== 0){
            let points = i + 1;
            let totalPoints = input[i].length * Number(input[points]) / 2;
            academyPoints += totalPoints
        }
        if(academyPoints > 1250.5){
            console.log(`Congratulations, ${actorName} got a nominee for leading role with ${academyPoints.toFixed(1)}!`)
            break;
        }
    }

    let diff = Math.abs(academyPoints- 1250.5);

    if(academyPoints <= 1250.5){
        console.log(`Sorry, ${actorName} you need ${diff.toFixed(1)} more!`)
    }
}
oscars(["Sandra Bullock",
"340",
"5",
"Robert De Niro",
"50",
"Julia Roberts",
"40.5",
"Daniel Day-Lewis",
"39.4",
"Nicolas Cage",
"29.9",
"Stoyanka Mutafova",
"33"])
;
