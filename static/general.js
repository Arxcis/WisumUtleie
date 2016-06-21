



function Switchbox(argsList){

	/*-- CONSTANTS --*/
	this.argsList = argsList;
	this.argsLength = argsList.length;

	/*-- variables --*/
	this.stateIndex = 0;
	this.stateValue = argsList[0];

	/*-- Methods --*/
	this.forward = function(){

		if (this.stateIndex < this.argsLength - 1){
			this.stateIndex += 1;
			this.stateValue = this.argsList[this.stateIndex];

		} else {
			this.stateIndex = 0;
			this.stateValue = this.argsList[0];
		}; 
	};

	this.backward = function(){

		if(this.stateIndex > 0) {
			this.stateIndex -= 1;
			this.stateValue = this.argsList[this.stateIndex];

		} else {
			this.stateIndex = this.argsLength - 1;
			this.stateValue = this.argsList[this.stateIndex];
		};
	};

	this.specific = function(argIndex){

		this.stateIndex = argIndex;
		this.stateValue = this.argsList[argIndex]; 
	};	

	this.current = function(){
		return "The value is " + this.stateValue + " at switch: " + this.stateIndex;
	};

};

var switchBox1 = new Switchbox([true, false, true]);
var switchBox2 = new Switchbox([false, true, false]);



