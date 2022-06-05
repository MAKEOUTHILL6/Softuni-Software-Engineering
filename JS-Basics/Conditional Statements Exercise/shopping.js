function cart(input){
    let budget = Number(input[0]);
    let videoCards = Number(input[1]);
    let processors = Number(input[2]);
    let ram = Number(input[3]);

    let videoCardsPrice = videoCards * 250;
    let processorsPrice=  (videoCardsPrice * 0.35) * processors;
    let ramPrice = (videoCardsPrice * 0.1) * ram;

    let totalPrice = videoCardsPrice + processorsPrice + ramPrice;

    if(videoCards > processors){
        totalPrice = totalPrice * 0.85
    }

    diff = Math.abs(totalPrice - budget);

    if(budget > totalPrice){
        console.log(`You have ${diff.toFixed(2)} leva left!`)
    }
    else{
        console.log(`Not enough money! You need ${diff.toFixed(2)} leva more!`)
    }
}
cart(["920.45",
"3",
"1",
"1"])
;