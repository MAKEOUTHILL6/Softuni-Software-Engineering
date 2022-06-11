function trekking(input){
    let groupsCount = Number(input[0]);
    let totalPeople = 0;
    let inputL = input.length
    let musalaCount = 0;
    let monblanCount = 0;
    let kilimanjaroCount = 0;
    let k2Count = 0;
    let everestCount = 0;

    for(let i=1; i<inputL; i++){
        let currentPerson = Number(input[i])
        totalPeople += currentPerson;
        if(currentPerson <= 5){
            musalaCount += currentPerson;
        }
        else if(currentPerson >= 6 && currentPerson <=12){
            monblanCount += currentPerson;
        }
        else if(currentPerson >=13 && currentPerson <= 25){
            kilimanjaroCount += currentPerson;
        }
        else if(currentPerson >=26 && currentPerson <= 40){
            k2Count += currentPerson;
        }
        else if(currentPerson >=41){
            everestCount += currentPerson;
        }
    }
    let musalaPercent = (musalaCount / totalPeople) * 100;
    let monblanPercent = (monblanCount / totalPeople) * 100;
    let kilimanjaroPercent = (kilimanjaroCount / totalPeople) * 100;
    let k2Percent = (k2Count / totalPeople) * 100;
    let everestPercent = (everestCount / totalPeople) * 100;
    console.log(`${musalaPercent.toFixed(2)}%`);
    console.log(`${monblanPercent.toFixed(2)}%`);
    console.log(`${kilimanjaroPercent.toFixed(2)}%`);
    console.log(`${k2Percent.toFixed(2)}%`);
    console.log(`${everestPercent.toFixed(2)}%`);
}
trekking(["5",
"25",
"41",
"31",
"250",
"6"])
;
