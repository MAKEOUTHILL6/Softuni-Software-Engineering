function game(input){
    let info = input[0].split("|")
    let health = 100;
    let coins = 0;
    let isDead = false;
    let counterRoom = 0;
    for(let i=0; i<info.length; i++){
        let roomInfo = info[i].split(" ");
        let command = roomInfo[0];
        let num = Number(roomInfo[1]);
        counterRoom++;
        if(command === "potion"){
            if(health + num > 100){
                num = 100 - health;
                health = 100;
            }else{
                health += num;
            }
            console.log(`You healed for ${num} hp.`);
            console.log(`Current health: ${health} hp.`);
        }
        else if(command === "chest"){
            coins += num;
            console.log(`You found ${num} coins.`);
        }
        else{
            health -= num;
            if(health > 0){
                console.log(`You slayed ${command}.`);
            }
            else{
                console.log(`You died! Killed by ${command}.`);
                console.log(`Best room: ${counterRoom}`);
                isDead = true;
                break;
            }
        }
    }
    if(isDead === false){
        console.log(`You've made it!`);
        console.log(`Coins: ${coins}`);
        console.log(`Health: ${health}`); 
    }
}
game(["cat 10|potion 30|orc 10|chest 10|snake 25|chest 110"]);