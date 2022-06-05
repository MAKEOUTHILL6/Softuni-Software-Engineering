function record(input){
    let recordInSeconds = Number(input[0]);
    let distanceInMeters = Number(input[1]);
    let timeInSeconds = Number(input[2]);

    let neededDistance = distanceInMeters * timeInSeconds;
    let slow = Math.floor(distanceInMeters / 15);
    let totalTime = (slow * 12.5) + neededDistance;
    let diff = Math.abs(totalTime - recordInSeconds);
    if(totalTime < recordInSeconds){
        console.log(`Yes, he succeeded! The new world record is ${totalTime.toFixed(2)} seconds.`)
    }
    else{
        console.log(`No, he failed! He was ${diff.toFixed(2)} seconds slower.`)
    }
}
record(["55555.67",
"3017",
"5.03"])
;
