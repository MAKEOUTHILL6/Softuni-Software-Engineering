function seq(input){
    let word = input[0];
    let sum = 0;
    for(let a=0; a<word.length; a++){
        if(word[a] === "a"){
            sum += 1;
        }
        else if(word[a] === "e"){
            sum += 2;
        }
        else if(word[a] === "i"){
            sum += 3;
        }
        else if(word[a] === "o"){
            sum += 4;
        }
        else if(word[a] === "u"){
            sum += 5;
        }
    }
    console.log(sum);
}
seq(["hi"]);