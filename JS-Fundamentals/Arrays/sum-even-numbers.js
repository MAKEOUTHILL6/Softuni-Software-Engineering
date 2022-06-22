function solve(arr){
    let res = 0;
    for(let i=0; i<arr.length; i++){
        num = Number(arr[i]);
        if(num % 2 === 0){
            res += num;
        }
    }
    console.log(res);

}
solve(['1','2','3','4','5','6']);