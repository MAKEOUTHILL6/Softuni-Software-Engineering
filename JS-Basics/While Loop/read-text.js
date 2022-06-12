function read(input){
    let index = 0;   
    let inputL = input.length;
    while(index <= inputL){
        let text = input[index]
        if(text == "Stop"){
            break;
        }
        console.log(text)
        index++
    }
}   
read(["Nakov",
"SoftUni",
"Sofia",
"Bulgaria",
"SomeText",
"Stop",
"AfterStop",
"Europe",
"HelloWorld"]);
