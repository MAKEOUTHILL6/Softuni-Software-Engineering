function calc(start, end){
    let totalSum = 0;
    let printLine = '';
    for(let i=start; i<=end; i++){
        totalSum += i;
        printLine += i + " ";
    }
    console.log(`${printLine}`);
    console.log(`Sum: ${totalSum}`);
}
calc(5, 10);