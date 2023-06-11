# look-im-hacking 
### Description

> A jump back into time to something that looks old! However, despite the looks, its not as old as it seems...

### Writeup
View source and we will see this function
```js
function loadFlag() {
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function () {
        document.getElementById("reveal").innerHTML = this.responseText;
    }
    xhttp.open("GET", "./flag.txt")
    xhttp.send();
}
```
well, we know that there is `flag.txt` and we can get that by executing this code.
So `open console` in browser and run the function adn we will get the flag.

![](https://i.imgur.com/DLXKZmA.png)

Flag: `jctf{$Hacker&?r3@L$}`