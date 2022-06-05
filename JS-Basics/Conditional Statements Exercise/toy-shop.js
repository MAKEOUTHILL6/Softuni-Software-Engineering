function shop(input){
    let excursionPrice = Number(input[0]);
    let puzzelPrice = 2.60 * Number(input[1]);
    let dollsPrice = 3 * Number(input[2]);
    let teddyBearPrice = 4.10 * Number(input[3]);
    let minionPrice = 8.20 * Number(input[4]);
    let truckPrice = 2 * Number(input[5]);

    let totalPrice = puzzelPrice + dollsPrice + teddyBearPrice + minionPrice + truckPrice;
    let countToys = Number(input[1]) + Number(input[2]) + Number(input[3]) + Number(input[4]) + Number(input[5]);
    if(countToys >= 50){
        totalPrice = totalPrice - (totalPrice * 0.25);
    }
    let profit = totalPrice - (totalPrice * 0.1);
    let left = 0;
    if(profit > excursionPrice){
        left = profit - excursionPrice;
        console.log(`Yes! ${left.toFixed(2)} lv left.`);
    }
    else{
        left = Math.abs(profit - excursionPrice);
        console.log(`Not enough money! ${left.toFixed(2)} lv needed.`);
    }
}
shop(["320",
"8",
"2",
"5",
"5",
"1"])
;
