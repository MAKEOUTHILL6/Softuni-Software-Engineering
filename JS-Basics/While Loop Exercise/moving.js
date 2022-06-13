function calc(input){
    let index = 0;
    let spaceWidth = Number(input[index]);
    index++;
    let spaceLength = Number(input[index]);
    index++;
    let spaceHeight = Number(input[index]);
    index++;
    let totalSpace = spaceHeight * spaceLength * spaceWidth;
    let command = input[index];
    let isSuccessful = true;
    let sumSpace = 0;
    while(command !== "Done"){
        let currentBox = Number(command);
        sumSpace += currentBox
        if(sumSpace >= totalSpace){
            console.log(`No more free space! You need ${Math.abs(sumSpace - totalSpace)} Cubic meters more.`);
            isSuccessful = false;
            break;
        }
        index++;
        command = input[index];
    }
    if(isSuccessful){
        console.log(`${Math.abs(sumSpace - totalSpace)} Cubic meters left.`)
    }
}
calc(["10", 
"1",
"2",
"4", 
"6",
"Done"])


;
