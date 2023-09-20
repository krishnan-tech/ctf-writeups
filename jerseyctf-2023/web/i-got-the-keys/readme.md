# i-got-the-keys
### Description
> Our receivers are picking up some intergalactic communication from a galaxy millions of light years away. This could be the major key we've been looking for!

### Writeup
After seeing the source, we got `authorization_key`
```js 
var endpoint = 'test'
fetch(window.location.href + endpoint, {
  headers: {
    'authorization_key': 'GdERHpBh3x'
  }
})
  .then(response => response.json())
  .then(data => {
    console.log(data);
    document.getElementById("api-response").innerHTML = JSON.stringify(data[endpoint]);
})
.catch(error => console.error(error));
```
But, unfortunately there is no other endpoints listed in source.
Therefore, I fuzzed the endpoint using gobuster using, 
`gobuster dir -u https://jerseyctf-i-got-the-keys.chals.io/ -w /usr/share/wordlists/dirb/common.txt`

And guess what? found the endpoint, and after requesting that endpoint with the `authorization_key` we got the flag.

![](https://i.imgur.com/BdUpjwr.png)

Flag: `jctf{*MAJ0R-K3Y-AL3RT*}`