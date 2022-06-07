function house(input){
    let flowerType = input[0];
    let flowerCount = Number(input[1]);
    let budget = Number(input[2]);
    let flowerPrice = 0;
    if(flowerType === "Roses"){
        if(flowerCount > 80){
            let rosePrice = flowerCount * 5;
            flowerPrice = rosePrice - (rosePrice * 0.1);
        }
        else{
            let rosePrice = flowerCount * 5;
            flowerPrice = rosePrice
        }
    }
    else if(flowerType === "Dahlias"){
        if(flowerCount > 90){
            let dahliaPrice = flowerCount * 3.80;
            flowerPrice = dahliaPrice - (dahliaPrice * 0.15);
        }
        else{
            let dahliaPrice = flowerCount * 3.80;
            flowerPrice = dahliaPrice;
        }
    }
    else if(flowerType === "Tulips"){
        if(flowerCount > 80){
            let tulipPrice = flowerCount * 2.80;
            flowerPrice = tulipPrice - (tulipPrice * 0.15);
        }
        else{
            let tulipPrice = flowerCount * 2.80;
            flowerPrice = tulipPrice;
        }
    }
    else if(flowerType === "Narcissus"){
        if(flowerCount < 120){
            let narcissusPrice = flowerCount * 3;
            flowerPrice = narcissusPrice + (narcissusPrice * 0.15);
        }
        else{
            let narcissusPrice = flowerCount * 3;
            flowerPrice = narcissusPrice;
        }
    }
    else if(flowerType === "Gladiolus"){
        if(flowerCount < 80){
            let gladiolusPrice = flowerCount * 2.50;
            flowerPrice = gladiolusPrice + (gladiolusPrice * 0.20);
        }
        else{
            let gladiolusPrice = flowerCount * 2.50;
            flowerPrice = gladiolusPrice;
        }
    }
    let diff = Math.abs(flowerPrice - budget);

    if(budget >= flowerPrice){
        console.log(`Hey, you have a great garden with ${flowerCount} ${flowerType} and ${diff.toFixed(2)} leva left.`)
    }
    else{
        console.log(`Not enough money, you need ${diff.toFixed(2)} leva more.`)
    }
    
}
house(["Narcissus",
"119",
"360"])
;
