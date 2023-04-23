var contentDivs = document.querySelectorAll(".sliddingDivs, .appearingDivs, .slidingAppearingDivsRight, .slidingAppearingDivsLeft","index_car_container");
var car = document.getElementById('car');
var car_width = parseFloat(getComputedStyle(car).getPropertyValue('width'))

window.addEventListener('load', onload);
window.addEventListener('scroll', checkContentDivs,false);

checkContentDivs();

function checkContentDivs() {
    var triggerHeight = window.innerHeight;

    contentDivs.forEach(function(div) {
        var divTop = div.getBoundingClientRect().top;
        if (divTop < triggerHeight) {
            div.classList.add('show');
        } else {
            div.classList.remove('show');
        }
    });
    moveCar(car);
}

function moveCar(car){
    var scroll = $(document).scrollTop();
    let width = window.innerWidth-car_width;
    var scrollableHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight
    let percentage = (scroll-scrollableHeight/2) / (scrollableHeight/2);
    let move = percentage*width;
    if (move > 0){
        car.style.left = (move) + "px";
        /* car.style.left = (move-car_width) + "px"; */
    }
}

function revealMap(element,map_name){
    let map = document.getElementById(map_name);
    map.style.display = 'block';
    element.style.display = 'none';
}

function changeWindowStyle(){
    let window = document.getElementsByTagName('body')[0];
    window.style = 'height: auto!important;overflow-x: hidden!important;'
}

function loadingAnimations(){
    let divs = document.getElementsByClassName('loading_animation');

    for (let div of divs){
        div.classList.add('show');
    }
}

function onload(){
    changeWindowStyle();
    loadingAnimations();
}
