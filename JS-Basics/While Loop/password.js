function password(input){
    let index = 2;
    let name = input[0];
    let pass = input[1];
    let inputL = input.length;

    while(index <= inputL){
        let current_pass = input[index];

        if(current_pass === pass){
            console.log(`Welcome ${name}!`);
            break;
        }
        else{
            index++
            continue;
        }
    }   
}
password(["Gosho",
"secret",
"secret"])
;
