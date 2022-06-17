function maining(input){
    let kgGold = 67.51;
    let oneBitcoin = 11949.16;
    let inputL = input.length;
    let index = 0;
    let goldPerDay = input[index];
    index++;
    let totalSum = 0;
    let firstDay = 0;
    let boughtCoins = 0;
    let priceBoughtCoin = 0;
    let sumBitcoints = 0;
    let boughtFirstDay = false;
    for(let i=1; i<=inputL; i++){
       let temp_sum = 0;
       if(i % 3 === 0){
        temp_sum += goldPerDay * kgGold - (goldPerDay * kgGold * 0.3);
       }
       else{temp_sum += goldPerDay * kgGold}
       totalSum += temp_sum
       if(totalSum >= oneBitcoin){
            boughtCoins++;
            priceBoughtCoin = Math.floor(totalSum / oneBitcoin);
            totalSum -= priceBoughtCoin * oneBitcoin
            sumBitcoints += priceBoughtCoin;

        if(boughtFirstDay === false){
            boughtFirstDay = true;
            firstDay += i
        }
    }  
       goldPerDay = input[index++];
    }
    console.log(`Bought bitcoins: ${sumBitcoints}`);
    if(boughtFirstDay === true){
        console.log(`Day of the first purchased bitcoin: ${firstDay}`);
    }
    console.log(`Left money: ${totalSum.toFixed(2)} lv.`)
}
maining([100, 200, 300]);