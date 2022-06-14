function building(input){
    let buildingFloors = Number(input[0]);
    let apsPerFloor = Number(input[1]);

    for(let floor = buildingFloors; floor > 0; floor--){
        let floorString = '';
        for(let room = 0; room < apsPerFloor; room++){
            if(floor === buildingFloors){
                floorString += "L" + floor + room + " ";
            }
            else if(floor % 2 === 0){
                floorString += "O" + floor + room + " ";
            }
            else{
                floorString += "A" + floor + room + " ";
            }
        }
        console.log(floorString)
    }
}
building(["6", "4"]);