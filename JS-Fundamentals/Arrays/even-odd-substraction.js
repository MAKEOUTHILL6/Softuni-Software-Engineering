function solve(arr){
    let sum_even = 0;
    let sum_odd = 0;
    let res = 0;
    for(let i = 0; i<arr.length; i++){
        if(arr[i] % 2 === 0){
            sum_even += arr[i];
        }else{
            sum_odd += arr[i];
        }
    }
    res = sum_even - sum_odd;
    console.log(res);
}
solve([1,2,3,4,5,6]);