function balance(input){
    let index = 0;
    let total = 0;
    let inputL = input.length;
    while(index <= inputL){
        let current_action = input[index];
        index++
        if(current_action === "NoMoreMoney"){
            console.log(`Total: ${total.toFixed(2)}`);
            break;
        }
        else{
            current_action_number = Number(current_action);
            if(current_action_number < 0){
                console.log("Invalid operation!")
                console.log(`Total: ${total.toFixed(2)}`);
                break;
            }
            else{
                console.log(`Increase: ${current_action_number.toFixed(2)}`);
                total += current_action_number;
            }
        }
    }
}
balance(["120",
"45.55",
"-150"])
;
