# Cyber Apocalypse 2023 writeup

## Trapped Source (WEB)

Description: Intergalactic Ministry of Spies tested Pandora's movement and intelligence abilities. She found herself locked in a room with no apparent means of escape. Her task was to unlock the door and make her way out. Can you help her in opening the door?

## Writeup

Check the source, and we will find this chunk of code
```js
<script>
    window.CONFIG = window.CONFIG || {
        buildNumber: "v20190816",
        debug: false,
        modelName: "Valencia",
        correctPin: "8291",
    }
</script>
```

There it is, our correct pin!

On entering the pin, we will get the flag.

## Flag: 
`HTB{V13w_50urc3_c4n_b3_u53ful!!!}`
