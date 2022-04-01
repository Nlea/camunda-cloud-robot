*** Settings ***
Documentation     Get a random destination

Library           RPA.Browser.Selenium


*** Tasks ***
Get a random destination
    Open Available Browser    https://earthroulette.com/
    Title Should Be    Earth Roulette - Random Holiday Generator. Generate a Random Vacation

    Click Element      //*[@class ="links"]

    #Wait Until Element is Visible    //*[@id = "card"]
    #Click Element      //*[@id = "dismiss-button"]

    Wait Until Element is Visible     //*[@class = "hero-body"]

    ${destination}=    Get Element Attribute    xpath://*[@class="title"]    innerHTML
    Sleep    5
    ${country}=        Get Element Attribute    xpath://*[@class="subtitle"]    innerHTML
    ${description}=    Get Element Attribute    xpath://*[@class="perex"]    innerHTML

    Log    ${destination} + ${country} + ${description}