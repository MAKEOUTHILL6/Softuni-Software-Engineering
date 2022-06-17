function division(num){
    let isDivisible = true;
    let biggest = 0;
    if(num % 2 === 0){
        biggest = 2;
    }
    if(num % 3 === 0){
        biggest = 3;
    }
    if(num % 6 === 0){
        biggest = 6;
    }
    if(num % 7 === 0){
        biggest = 7;
    }
    if(num % 10 === 0){
        biggest = 10;
    }
    if(num % 2 !== 0 && num % 3 !== 0 && num % 6 !== 0 && num % 7 !== 0 && num % 10 !== 0){
        console.log("Not divisible")
        isDivisible = false;
    }
    if(isDivisible){
        console.log(`The number is divisible by ${biggest}`);
    }
}
division(30)