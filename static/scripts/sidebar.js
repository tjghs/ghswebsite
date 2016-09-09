var mb = document.querySelector("#nav-button"),
    sb = document.querySelector("#sidebar"),
    wr = document.querySelector("#wrapper");
sb.style.disabled = true;
function toggleSidebar(toggleOpenAllowed) {
    if(sb.style.disabled && toggleOpenAllowed) {
        sb.style.disabled = false;
        sb.style.left = "0px";
        console.log("asdf");
    } else {
        sb.style.left = "-200px";
        sb.style.disabled = true;
    }
}
mb.addEventListener("click", function(){toggleSidebar(true)}, false);
wr.addEventListener("click", function(){toggleSidebar(false)}, false);
