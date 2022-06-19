function echo(input){
    let element = input;
    let elementType = typeof element;
    console.log(elementType);
    if(elementType === "string" || elementType === "number"){
        console.log(element);
    }
    else{
        console.log('Parameter is not suitable for printing');
    }
}
echo(null);