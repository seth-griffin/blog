function processTouchStart(event) {
	var touchobj = event.changedTouches[0];
	xDistanceTraveled = 0;
	yDistanceTraveled = 0;
	startX = touchobj.pageX;
	startY = touchobj.pageY;
	startTime = new Date().getTime();
	event.preventDefault();
	
	document.getElementById("debug").innerHTML = "Touch Start: <br>&nbsp;&nbsp;&nbsp;" + 
                                 "X: " + startX + 
                                 "<br>&nbsp;&nbsp;&nbsp;Y: " + startY + 
                                 "<br>&nbsp;&nbsp;&nbsp;Time: " + startTime.toString();

}

function processTouchMove(event) {
	var changedTouch = event.changedTouches[0];
	xDistanceTraveled = changedTouch.pageX - startX;
	yDistanceTraveled = changedTouch.pageY - startY;

	touchDuration = new Date().getTime() - startTime;

	document.getElementById("debug").innerHTML = "X: " + changedTouch.pageX + 
                                 "<br>Y: " + changedTouch.pageY + 
                                 "<br>Time: " + startTime.toString() + 
                                 "<br>Touch Duration: " + touchDuration.toString();

	if(xDistanceTraveled > yDistanceTraveled) {
		if(startX < 200 && xDistanceTraveled > 100 && changedTouch.pageX > 200) {
			document.getElementById("debug").innerHTML = "Right Swipe Detected!";
			swipeRightShowMobileMenu();
		}
		else {
			if(startX > 10 xDistanceTraveled > 100 && changedTouch.pageX > 200) {
				document.getElementById("debug").innerHTML = "Left Swipe Detected!";
				swipeLeftHideMobileMenu();
			}
		}

		event.preventDefault();
	}
}

function processTouchEnd(event) {
	startX = 0;
	startY = 0;
	startTime = 0; 
	xDistanceTraveled = 0;
	yDistanceTraveled = 0;
	touchDuration = 0;

	document.getElementById("debug").innerHTML = "Touch Ended!";
}

function showMobileMenuOn() {
	var mobileMenuButton = document.getElementById("mobile-menu");
	mobileMenuButton.src = "mobile-menu-on.png";
}

function showMobileMenuOff() {
	var mobileMenuButton = document.getElementById("mobile-menu");
	mobileMenuButton.src = "mobile-menu.png";
}

function swipeRightShowMobileMenu() {
	showMobileMenuOn();
	nav.style.display = "block";
}

function swipeLeftHideMobileMenu() {
	showMobileMenuOff();
	nav.style.display = "none";                    
}

function toggleMobileMenu(event) {
	var nav = document.getElementById('nav');
	if(nav.style.display == 'block') {
		showMobileMenuOff();
		nav.style.display = 'none';
	}
	else {
		showMobileMenuOn();
		nav.style.display = 'block';
	}
}

function init() {
	document.getElementById("mobile-menu").addEventListener("click", toggleMobileMenu, false);
	//document..addEventListener("touchstart", processTouchStart, false);
	//document.body.addEventListener("touchmove", processTouchMove, false);
	//document.body.addEventListener("touchend", processTouchEnd, false);
}

window.addEventListener("load", init, false);
window.addEventListener("scroll", 
        function(event) {
            if(window.pageYOffset >= 171) {
                document.getElementById("top").style.visibility = "visible";
            } 
            else {
                document.getElementById("top").style.visibility = "hidden";
            }
        },
        false
);
