function fishing(input){
    let budget = Number(input[0]);
    let season = input[1];
    let fishers = Number(input[2]);
    let pricePerSeason = 0;
    let discount = 0;
    let totalPrice = 0;
    let diff = 0;

    if(season === "Spring"){
        pricePerSeason = 3000;
    }
    else if(season === "Summer" || season === "Autumn"){
        pricePerSeason = 4200;
    }
    else if(season === "Winter"){
        pricePerSeason = 2600;
    }

    if(fishers % 2 === 0 && season !== "Autumn"){
        discount += 0.05
    }
    if(fishers <= 6){
        discount += 0.1
    }
    else if(fishers >= 7 && fishers <= 11){
        discount += 0.15
    }
    else{
        discount += 0.25
    }

    totalPrice = pricePerSeason - (pricePerSeason * discount);
    diff = Math.abs(totalPrice - budget);

    if(budget >= totalPrice){
        console.log(`Yes! You have ${diff.toFixed(2)} leva left.`);
    }
    else{
        console.log(`Not enough money! You need ${diff.toFixed(2)} leva.`);
    }

}
fishing(["2000",
"Winter",
"13"])
;
