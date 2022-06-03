function pass(input){
    let guess = input[0];
    let specialPass = "s3cr3t!P@ssw0rd";
    if(guess === specialPass){
        console.log("Welcome")
    }
    else{
        console.log("Wrong password!")
    }
}
pass(["qwerty"]);