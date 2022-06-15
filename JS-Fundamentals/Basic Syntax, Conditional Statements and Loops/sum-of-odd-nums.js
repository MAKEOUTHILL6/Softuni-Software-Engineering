function calc(n){
    let result = 0;
    for(let i=1; i<=n * 2; i+=2){
        result += i;
        console.log(i);
    }
    console.log(`Sum: ${result}`);
}
calc(3);