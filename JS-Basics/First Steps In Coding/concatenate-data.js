function data(input){
    let name = input[0];
    let secondName = input[1];
    let age = input[2];
    let town = input[3];
    console.log(`You are ${name} ${secondName}, a ${age}-years old person from ${town}.`);
}
data(["Martin", "Atanasov", 17, "Sofia"]);