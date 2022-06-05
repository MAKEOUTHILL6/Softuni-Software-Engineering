function move(input){
    let movieBudget = Number(input[0]);
    let statists = Number(input[1]);
    let clothing = Number(input[2]);

    let decorPrice = movieBudget * 0.1;
    let clothingPrice = clothing * statists;
    if(statists > 150){
        clothingPrice = clothingPrice * 0.9;
    }
    let totalPrice = clothingPrice + decorPrice;
    let left = Math.abs(totalPrice - movieBudget);
    if(totalPrice < movieBudget){
        console.log("Action!");
        console.log(`Wingard starts filming with ${left.toFixed(2)} leva left.`)
    }
    else{
        console.log("Not enough money!");
        console.log(`Wingard needs ${left.toFixed(2)} leva more.`)
    }

}
move(["9587.88",
"222",
"55.68"])

