function login(input){
    let index = 0;
    let userName = input[index];
    index++;
    let password = [...userName].reverse().join("");
    let tries = 0;
    let command = input[index];
    index++;
    let isSuccessful = true;
    while(command !== password){
        if(command !== password){
            tries += 1;
            if(tries === 4){
                isSuccessful = false;
                console.log(`User ${userName} blocked!`);
                break;
            }
            console.log("Incorrect password. Try again.");
        }
        command = input[index++]
    }
    if(isSuccessful){
        console.log(`User ${userName} logged in.`);
    }
    
}
login(['sunny','rainy','cloudy','sunny','not sunny']);