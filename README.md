# lg_magic_ble
Discoveries reverses engineering the BLE HID descriptors

HID raw stream breaks up in 20 byte segments

## Updated findings

I'm breaking this into decimal so it's easier to parse.

The only motion data that is consistent is the 12th byte. I can twist the remote in my hand and get a flat value of 0 and ~240 left 90 degress and 15 right 90 degress.

The rest seems like raw acceleromter data.

```
253       Constant
214       Unknown (range of about 180 to 220)
49        Counter (00 to FF incremenmnts every message
253       Constant
0         Constant
255       Motion
237       Motion 
255       Motion
248       Motion
255       Motion
255       Motion
0         Motion (Roll along X axis)
32        Motion 
254       Motion
107       Motion
240       Motion
45        Motion
0         Is button pressed (0 or 128)
0         Button code
0         Scrollwheel (Up 1, Down 255)
```

Keymap
| Button | Hex |
| ------------- | ------------- |
| 1  | 11 |
| 2  | 12 |
| 3  | 13 |
| 4  | 14 |
| 5  | 15 |
| 6  | 16 |
| 7  | 17 |
| 8  | 18 |
| 9  | 19 |
| 0  | 10 |
| LIST  | 4C |
| QAM  | 45 |
| Vol Up  | 02 |
| Vol Down  | 03 |
| Chan Uo  | 00 |
| Chan Down  | 01 |
| Mute  | 09 |
| Mic  | 8B |
| Home  | 7C |
| Input  | 0B |
| Up  | 40 |
| Down  | 41 |
| Left  | 07 |
| Right  | 06 |
| Wheel click  | 44 |
| Back  | 28 |
| Settings  | 43 |
| Red  | 72 |
| Green  | 71 |
| Yellow  | 63 |
| Blue  | 61 |
| App 1  | 56 |
| App 2  | 5C |
| App 3  | 31 |
| App 4  | 48 |
| App 5  | 05 |
| App 6  | 0C |

## Intiial findings

```
FD                DCB6FDFFFFEFFFFAFFFE0028FE65F027        00   00     00
Constant          Gyro fuckery                            Buttons     Scrollwheel
```

Hex mapping for the MR21 remote

![alt text](Untitled.png)
