function calc(input){
    let index = 0;
    let biggest = Number.MIN_SAFE_INTEGER;
    let inputL = input.length;
    while(index <= inputL){
        let current_element = input[index]
        index++
        if(current_element === "Stop"){
            console.log(biggest);
            break;
        }
        else{
            let current_element_num = Number(current_element);
            if(current_element_num > biggest){
                biggest = current_element_num;
            }
        }
    }
}
calc(["45",
"-20",
"7",
"99",
"Stop"])
;
