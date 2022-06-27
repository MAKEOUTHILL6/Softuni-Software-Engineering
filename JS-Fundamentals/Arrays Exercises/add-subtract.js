function solve(arr){
    let modifiedArr = []
    for(let i=0; i<arr.length; i++){
        if(arr[i] % 2 === 0){
            let el = arr[i] + i;
            modifiedArr.push(el);
        }else{
            let el = arr[i] - i;
            modifiedArr.push(el);
        }
    }
    console.log(modifiedArr)

    let sumOriginalArr = 0;
    for(let i=0; i<arr.length; i++){
        sumOriginalArr += arr[i];
    }
    console.log(sumOriginalArr);

    let sumNewArr = 0;
    for(let i=0; i<modifiedArr.length; i++){
        sumNewArr += modifiedArr[i];
    }
    console.log(sumNewArr);

}
solve([-5, 11, 3, 0, 2]);