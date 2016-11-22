"use strict"
var left = document.querySelector("#left-arrow"),
    right = document.querySelector("#right-arrow"),
    ss = document.querySelector("#slideshow");


var script = document.createElement("script"),
    linkArr = [],
    index = 0;

script.src = "https://api.flickr.com/services/rest/?method=flickr.people.getPhotos&api_key=cebede3e2c905c250355e3755eca032c&user_id=144387717%40N03&extras=url_c%2Curl_o&format=json";
document.getElementById("wrapper").appendChild(script);

function jsonFlickrApi(data) {
    var photos = data.photos.photo;
    for (var i = 0; i < photos.length; i++) {
        linkArr.push([photos[i].url_c, photos[i].url_o]);
        console.log(photos[i].url_c);
    }
}

function getLeftImage() {
    if(index > 0) {
        index--;
    }
    console.log(index);
    console.log(ss.lastElementChild.src);
    ss.lastElementChild.src = linkArr[index][0];
}

function getRightImage() {
    if(index < linkArr.length - 1) {
        index++;
    }
    console.log(index);
    console.log(ss.lastElementChild.src);
    ss.lastElementChild.src = linkArr[index][0];
}


left.addEventListener("click", function(){getLeftImage()}, false);
right.addEventListener("click", function(){getRightImage()}, false);
left.addEventListener("touchleave", function(){getLeftImage()}, false);
right.addEventListener("touchleave", function(){getRightImage()}, false);
/*function loadMore() {
    var temp = imgNum,
    	loadNum = (2 * Math.floor((window.innerWidth - 296) / 325)) == 0 ? 2 : (2 * Math.floor((window.innerWidth - 296) / 325));
    if (temp + loadNum > linkArr.length) {
        for (var i = imgNum; i < linkArr.length; i++) {
            imgMod.push(new imgModule(linkArr[linkArr.length - i - 1], capArr[capArr.length - i - 1]));
            imgNum++;
        }
        document.getElementById("load-more").style.display = "none";
    } else {
        for (var i = imgNum; i < temp + loadNum; i++) {
            imgMod.push(new imgModule(linkArr[linkArr.length - i - 1], capArr[capArr.length - i - 1]));
            imgNum++;
        }
    }
}*/

/*function expandImage(url, cap) {
    var gallery = document.getElementById("gallery"),
        galleryWrap = document.getElementById("gallery-wrapper");
    gallery.innerHTML = "";
    gallery.style.visibility = "visible";
    galleryWrap.style.opacity = "1";
    galleryWrap.style.visibility = "visible";
    document.getElementById("gallery-caption").innerHTML = cap;

    var img = new Image();
    img.src = url;
    var preload = document.createElement("div");
    preload.className = "md-preloader";
    preload.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" version="1.1" height="75" width="75" viewbox="0 0 75 75"><circle cx="37.5" cy="37.5" r="33.5" stroke-width="8"/></svg>';
    var checkLoad = window.setInterval(function() {
        isLoad = img.complete;
        if (gallery.firstChild == null) {
            gallery.appendChild(preload);
        }
        if (isLoad) {
            gallery.innerHTML = "";
            gallery.appendChild(img);
            gallery.style.cursor = "zoom-in";
            window.clearInterval(checkLoad);
        }
    }, 100);
}*/

/*window.onload = function() {
	var initNum = (Math.floor((window.innerWidth - 296) / 325)) == 0 ? 1 : (2 * Math.floor((window.innerWidth - 296) / 325));
    for (var i = imgNum; i < 4 * initNum; i++) {
        imgMod.push(new imgModule(linkArr[linkArr.length - i - 1], capArr[capArr.length - i - 1]));
        imgNum++;
    }
}*/
/*
gallery.ondblclick = function() {
    if(isLoad) {
        if(isZoom) {
            gallery.style.cursor = "zoom-in";
            this.style.transform = "scale(1)";
            this.style.top = "0px";
            this.style.left = "0px";
        } else {
            gallery.style.cursor = "zoom-out";
            this.style.transform = "scale(2)";*/
            /*this.style.top = 2 * event.y + "px";
            this.style.left = 2 * event.x + "px";*/     
        /*}
        isZoom = !isZoom;
    }
}

function imgModule(url, cap) {
        this.url = url[0];
        this.orig = url[1];
        var parent = document.getElementById("content"),
            imgCard = document.createElement("div"),
            mod = document.createElement("div"),
            bar = document.createElement("div"),
            label = document.createElement("div");
        imgCard.className = "image-card";
        imgCard.style.backgroundImage = "url(" + url[0] + ")";
        imgCard.onclick = function() {
            expandImage(url[1], cap);
        };
        mod.className = "";
        bar.className = "info-overlay";
        label.className = "info-text";
        label.innerHTML = cap;
        imgCard.appendChild(bar);
        bar.appendChild(label);
        imgCard.appendChild(mod);
        parent.insertBefore(imgCard, document.getElementById("load-more"));
}*/
