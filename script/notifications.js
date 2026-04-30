/**
 * Module that registers the notification box and handles messages
 */

class NotifyMessage {
	constructor(text, color, isBold) {
		this.text = text;
		this.color = color;
		this.isBold = isBold;
	}
}

var Notifications = {
	
	init: function(options) {
		this.options = $.extend(
			this.options,
			options
		);
		
		// Create the notifications box
		elem = $('<div>').attr({
			id: 'notifications',
			className: 'notifications'
		});
		// Create the transparency gradient
		$('<div>').attr('id', 'notifyGradient').appendTo(elem);
		
		elem.appendTo('div#wrapper');
	},
	
	options: {}, // Nothing for now
	
	elem: null,
	
	notifyQueue: {},
	
	// Allow notification to the player
	notify: function(module, text, color, isBold, noQueue) {
		if(typeof text == 'undefined') return;
		if(text.slice(-1) != ".") text += ".";
		if(module != null && Engine.activeModule != module) {
			if(!noQueue) {
				if(typeof this.notifyQueue[module] == 'undefined') {
					this.notifyQueue[module] = [];
				}
				let msgObj = new NotifyMessage(text, color, isBold);
				this.notifyQueue[module].push(msgObj); // push msg object into queue
			}
		} else {
			Notifications.printMessage(text, color, isBold);
		}
		Engine.saveGame();
	},
	
	clearHidden: function() {
	
		// To fix some memory usage issues, we clear notifications that have been hidden.
		
		// We use position().top here, because we know that the parent will be the same, so the position will be the same.
		var bottom = $('#notifyGradient').position().top + $('#notifyGradient').outerHeight(true);
		
		$('.notification').each(function() {
		
			if($(this).position().top > bottom){
				$(this).remove();
			}
		
		});
		
	},
	
	printMessage: function(t, color, isBold) {
		if(color == null) {
			console.log("defaultni barva");
			color = "#000000";
		}
		if(isBold == null || isBold == false) {
			isBold = "normal";
		}
		else {
			isBold = "bold";
		}
		var text = $('<div>').addClass('notification')
							.css({
								'opacity': '0',
								'color': `${color}`,
								'font-weight': `${isBold}`
							})
							.text(t)
							.prependTo('div#notifications');
		text.animate({opacity: 1}, 500, 'linear', function() {
			// Do this every time we add a new message, this way we never have a large backlog to iterate through. Keeps things faster.
			Notifications.clearHidden();
		});
	},
	
	printQueue: function(module) {
		if (typeof this.notifyQueue[module] != 'undefined') {
			while (this.notifyQueue[module].length > 0) {
				let msgObj = this.notifyQueue[module].pop();
				Notifications.printMessage(msgObj.text, msgObj.color, msgObj.isBold); // show with color
			}
		}
	}	
};
