let village=require("./village.js");

function animate(state,robot,memory,count) {
    // your code goes here.
    console.log('\033c');
    console.log(state.toString());
    console.log("Turn: " + count);
    if(state.parcels.length > 0) {
        let action = robot(state, memory);
        let newState = state.move(action.direction);
        let newMemory = action.memory;
        let newCount = count + 1;
        setTimeout(
            function() {
                animate(newState, newMemory, newCount);
            },
            1000);
    }
}

animate(village.VillageState.random(9), village.randomRobot,[],0);