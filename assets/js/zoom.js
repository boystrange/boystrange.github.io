function zoom(containerID, imgID) {
    var container = document.getElementById(containerID);
    var img = document.getElementById(imgID);
    container.addEventListener("mouseenter", mouseEnter);
    container.addEventListener("mouseleave", mouseLeave);
    container.addEventListener("mousemove", mouseMove);
    /* And also for touch screens: */
    // img.addEventListener("touchmove", moveLens);

    function mouseEnter(e) {
	var box = container.getBoundingClientRect()
	console.log(box);
	container.style.maxWidth = box.width + "px";
	container.style.maxHeight = box.height + "px";
	e.preventDefault();
	img.style.width = "200%";
    }

    function mouseLeave(e) {
	e.preventDefault();
	container.style.removeProperty("max-width");
	container.style.removeProperty("max-height");
	img.style.width = "100%";
	img.style.top = "0px";
	img.style.left = "0px";
    }

    function mouseMove(e) {
	e.preventDefault();
	var pos = getCursorPos(e);
	img.style.left = "-" + pos.x + "px";
	img.style.top  = "-" + pos.y + "px";
    }

    function getCursorPos(e) {
	e = e || window.event;
	/* Get the x and y positions of the image: */
	var a = container.getBoundingClientRect();
	/* Calculate the cursor's x and y coordinates, relative to the image: */
	var x = e.pageX - a.left;
	var y = e.pageY - a.top;
	/* Consider any page scrolling: */
	x = x - window.pageXOffset;
	y = y - window.pageYOffset;
	return {x : x, y : y};
    }
}
