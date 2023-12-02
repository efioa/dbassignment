/*interactive map*/

async function getUser(place) {
    const api_url = 'https://timezone.abstractapi.com/v1/current_time/?api_key=cc12ff38f880451a80ec266a816818dc&location=${place}'
    
    const response = await fetch(api_url);
    
    const data = await response.json();
    
    time = await data.datetime
    // arr = Array.from(time)
    // arr.splice(0, 11)
    // timezone = (arr.splice(0, 5)).join("");
    document.getElementById("time").innerText = `${place}'s time = ${time} ${data.timezone_abbreviation}`

}

document.querySelectorAll(".allPaths").forEach(e => {
e.setAttribute('class', `allPaths ${e.id}`);
e.addEventListener("mouseover", function () {
    window.onmousemove=function (j) {
        x = j.clientX
        y = j.clientY
        document.getElementById('name').style.top = y-60  + 'px'
        document.getElementById('name').style.left = x +10 + 'px'
    }
    const classes=e.className.baseVal.replace(/ /g, '.')         
    document.querySelectorAll(`.${classes}`).forEach(country =>{
        country.style.fill = "pink"
    })
    document.getElementById("name").style.opacity = 1
    
    document.getElementById("namep").innerText = e.id
})
e.addEventListener("mouseleave", function () {
    const classes=e.className.baseVal.replace(/ /g, '.')
    document.querySelectorAll(`.${classes}`).forEach(country =>{
        country.style.fill = "#ececec"
    })
    document.getElementById("name").style.opacity = 0
})

e.addEventListener("click",function(){
    getUser(e.id)
})

})

