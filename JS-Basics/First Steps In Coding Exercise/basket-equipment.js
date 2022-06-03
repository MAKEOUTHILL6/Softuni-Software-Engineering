function equipment(input){
    let taxYear = Number(input[0]);
    let basketShoes = taxYear - (taxYear * 0.4);
    let basketFit = basketShoes - (basketShoes * 0.2);
    let basketBall = basketFit / 1/4;
    let basketAcc = basketBall / 1/5;
    let total = taxYear + basketShoes + basketFit + basketBall + basketAcc;
    console.log(total);
}
equipment(["365"]);