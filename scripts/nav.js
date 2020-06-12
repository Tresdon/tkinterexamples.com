// Creates the appropriate nav element for a page
const hierarchy = {
    "widgets": {
        "label": [],
        "frame": [],
        "button": []
    },
    "geometry": {
        "pack": [],
        "grid": [],
        "place": []
    }
}

function capitalize(str) {
    return str[0].toUpperCase() + str.substring(1)
}

const navDiv = document.getElementById("navigation")
const primaryNav = document.getElementById("primary")
const secondaryNav = document.getElementById("secondary")
const tertiaryNav = document.getElementById("tertiary")

function buildNav() {

    //ignore "http:", "", "tkinterexamples.com"
    let urlTokens = window.location.href.split("/").splice(3)
    // Ignore HTML page
    urlTokens.pop()

    // Always draw primary nav buttons
    let primaryKeys = Object.keys(hierarchy)
    for (key in primaryKeys) {
        let name = primaryKeys[key]
        // create element
        let elem = document.createElement("a")
        elem.appendChild(document.createTextNode(capitalize(name)))
        elem.setAttribute("href", `/${name}/${name}.html`)
        if (urlTokens[0] == name) {
            elem.classList.add("active")
        }
        primaryNav.appendChild(elem)
    }

    // If we're at level 1, draw level 2 nav
    if (urlTokens.length >= 1) {
        let firstLevel = urlTokens[0]
        let secondaryKeys = Object.keys(hierarchy[firstLevel])
        for (key in secondaryKeys) {
            let name = secondaryKeys[key]
            // create element
            let elem = document.createElement("a")
            elem.appendChild(document.createTextNode(capitalize(name)))
            elem.setAttribute("href", `/${firstLevel}/${name}/${name}.html`)
            if (urlTokens[1] == name) {
                elem.classList.add("active")
            }
            secondaryNav.appendChild(elem)
        }
    }


    // If we're at level 2, draw level 3 nav
    if (urlTokens.length >= 2) {
        let firstLevel = urlTokens[0]
        let secondLevel = urlTokens[1]
        let tertiaryKeys = hierarchy[firstLevel][secondLevel]
        for (key in tertiaryKeys) {
            let name = tertiaryKeys[key]
            // create element
            let elem = document.createElement("a")
            elem.appendChild(document.createTextNode(capitalize(name)))
            elem.setAttribute("href", `/${firstLevel}/${secondLevel}/${name}/${name}.html`)
            if (urlTokens[2] == name) {
                elem.classList.add("active")
            }
            tertiaryNav.appendChild(elem)
        }
    }

    
}

buildNav();
