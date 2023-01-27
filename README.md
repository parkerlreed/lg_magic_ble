# lg_magic_ble
Discoveries reverses engineering the BLE HID descriptors

HID raw stream breaks up in 20 byte segments

```
FD                DCB6FDFFFFEFFFFAFFFE0028FE65F027        00   00     00
Constant          Gyro fuckery                            Buttons     Scrollwheel
```

Hex mapping for the MR21 remote

![alt text](Untitled.png)
