function solve(word, char, secondWord){
    let finalString = word.replace("_", char);
    if(finalString === secondWord){
        console.log("Matched");
    }else{
        console.log("Not Matched");
    }
}
solve('Str_ng', 'I', 'Strong');