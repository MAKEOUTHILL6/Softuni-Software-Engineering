function solve(firstArr, secondArr){
    let thirdArr = [];
    for(let i=0; i<firstArr.length; i++){
        if(i % 2 === 0){
            thirdArr.push(Number(firstArr[i]) + Number(secondArr[i])); 
        }else{
            thirdArr.push(firstArr[i] + secondArr[i]);
        }
    }
    let res = []
    for(let i=0; i<thirdArr.length; i++){
        res.push(String(thirdArr[i]));
    }
    console.log(res.join(" - "));
}
solve(['5', '15', '23', '56', '35'],
['17', '22', '87', '36', '11']
);