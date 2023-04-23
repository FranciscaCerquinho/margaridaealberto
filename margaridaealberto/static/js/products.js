window.addEventListener('load',onload);
window.addEventListener('scroll', checkContentDivs,false);

function fillValueBars(){
    elements = document.getElementsByClassName("value_bar");
    for (element of elements){
        element.style.width = element.getAttribute('value') + "%"
    }
}

function checkContentDivs() {
    var contentDivs = document.querySelectorAll(".productSliddingDivs");
    var triggerHeight = window.innerHeight * 8/10;

    contentDivs.forEach(function(div) {
        var divTop = div.getBoundingClientRect().top;
        if (divTop < triggerHeight) {
            div.classList.add('show');
        } else {
            div.classList.remove('show');
        }
    });
}

function changeWindowStyle(){
    let window = document.getElementsByTagName('body')[0];
    window.style = 'height: auto!important;overflow-x: hidden!important;'
}

function onload(){
    changeWindowStyle();
    fillValueBars();
    checkContentDivs();
}