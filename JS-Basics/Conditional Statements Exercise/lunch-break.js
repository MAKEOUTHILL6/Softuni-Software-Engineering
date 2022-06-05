function chill(input){
    let serialName = input[0];
    let episodeDuration = Number(input[1]);
    let breakDuration = Number(input[2]);

    let lunchTime = breakDuration * 1/8;
    let chillTime = breakDuration * 1/4;

    let totalTime = breakDuration - lunchTime - chillTime;
    let diff = Math.ceil(Math.abs(totalTime - episodeDuration))
    if(totalTime >= episodeDuration){
        console.log(`You have enough time to watch ${serialName} and left with ${diff} minutes free time.`)
    }
    else{
        console.log(`You don't have enough time to watch ${serialName}, you need ${diff} more minutes.`)
    }
}
chill(["Teen Wolf",
"48",
"60"])
;