function calc(input){
    let index = 0;
    let cakeLength = Number(input[index]);
    index++;
    let cakeWidth = Number(input[index]);
    index++;
    let totalSlices = cakeLength * cakeWidth;
    let command = input[index];
    index++;
    let isEnough = true;
    while(command !== "STOP"){
        let currentSlice = Number(command);
        totalSlices -= currentSlice;
        if(totalSlices <= 0){
            console.log(`No more cake left! You need ${Math.abs(totalSlices)} pieces more.`);
            isEnough = false;
            break;
        }
        command = input[index];
        index++
    }
    if(isEnough){
        console.log(`${totalSlices} pieces are left.`);
    }
}
calc(["10",
"10",
"20",
"20",
"20",
"20",
"21"])

;
