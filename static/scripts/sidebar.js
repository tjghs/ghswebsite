var mb = document.querySelector("#nav-button"),
    sb = document.querySelector("#sidebar"),
    wr = document.querySelector("#wrapper");

mb.addEventListener("click", function(){toggleSidebar(true)}, false);
wr.addEventListener("click", function(){toggleSidebar(false)}, false);
mb.addEventListener("touchstart", function(){toggleSidebar(true)}, false);
wr.addEventListener("touchstart", function(){toggleSidebar(false)}, false);
sb.style.disabled = true;

function toggleSidebar(toggleOpenAllowed) {
    if((sb.style.disabled && toggleOpenAllowed) || (sb.style.right == "" && toggleOpenAllowed)) { //toggle
        sb.style.disabled = false;
        sb.style.right = "0px";
    } else { //untoggle
        sb.style.right = "-200px";
        sb.style.disabled = true;
    }
}
