function solve(firstArr, secondArr){
    matchedArr = []
    for(let el of firstArr){
        if(secondArr.includes(el)){
            matchedArr.push(el);
        }
    }
    console.log(matchedArr.join("\n"))
}
solve(['Hey', 'hello', 2, 4, 'Peter', 'e'],
['Petar', 10, 'hey', 4, 'hello', '2']
);