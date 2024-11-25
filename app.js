//1 problem///////////

const arr = [1,9,0,5];
Array.prototype.last = function() {
    if(this.length === 0){
        return -1;
    }else{
        return this[this.length - 1];
    }
};
/////////////////////////////
