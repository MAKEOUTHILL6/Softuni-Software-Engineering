function vacancy(input){
    let budget = Number(input[0]);
    let season = input[1];
    let summer = 0;
    let winter = 0;
    let totalPrice = 0;
    if(budget <= 100){
        if(season === "summer"){
            summer = budget - (budget * 0.3);
            totalPrice = budget - summer;
            console.log(`Somewhere in Bulgaria`);
            console.log(`Camp - ${totalPrice.toFixed(2)}`);
        }
        else if(season === "winter"){
            winter = budget - (budget * 0.7);
            totalPrice = budget - winter;
            console.log(`Somewhere in Bulgaria`);
            console.log(`Hotel - ${totalPrice.toFixed(2)}`);
        }
    }
    else if(budget <= 1000){
        if(season === "summer"){
            summer = budget - (budget * 0.4);
            totalPrice = budget - summer;
            console.log(`Somewhere in Balkans`);
            console.log(`Camp - ${totalPrice.toFixed(2)}`);
        }
        else if(season === "winter"){
            winter = budget - (budget * 0.8);
            totalPrice = budget - winter;
            console.log(`Somewhere in Balkans`);
            console.log(`Hotel - ${totalPrice.toFixed(2)}`);
        }
    }
    else if(budget > 1000){
        if(season === "summer"){
            summer = budget - (budget * 0.9);
            totalPrice = budget - summer;
            console.log(`Somewhere in Europe`);
            console.log(`Hotel - ${totalPrice.toFixed(2)}`);
        }
        else if(season === "winter"){
            winter = budget - (budget * 0.9);
            totalPrice = budget - winter;
            console.log(`Somewhere in Europe`);
            console.log(`Hotel - ${totalPrice.toFixed(2)}`);
        }
    }
}
vacancy(["1500", "summer"]);