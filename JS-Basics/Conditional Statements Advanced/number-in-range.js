function calc(input){
    let num = Number(input[0]);
    if(-100 <= num <= 100 && num !== 0){
        console.log("Yes");
    }
    else{
        console.log("No");
    }
}
calc(["-25"]);