function solve(arr){
    let newArr = [];
    for(let i=0; i<arr.length; i++){
       let firstNum = arr[i];
       let isLarger = true;
       for(let j=i+1; j<arr.length; j++){
        let secondNum = arr[j];

        if(firstNum <= secondNum){
            isLarger = false;
        }
       }
       if(isLarger){
        newArr.push(firstNum);
       }
    }
    console.log(newArr.join(" "));
}
solve([14, 24, 3, 19, 15, 17]);