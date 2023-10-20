# Denki-Mate

## Concept

This is a gamified approach to daily life. It allows children to connect with their parents' smartphones through a smartwatch or IoT device. They can raise an electronic creature within the device, fostering interaction and gameplay. Parents can provide electronic creature food to their children from the mobile app, allowing them to nurture their creatures.

When children request rewards, they can initiate creature challenges. If the creatures are well-cared for, they may succeed in these challenges. Parents can also adjust challenge levels and set rewards that motivate their children. Interactions with other children, battling with the creatures they've raised, create engaging gameplay.

Using AI image processing, children's artwork can be transformed into electronic creatures, enhancing the emotional connection between them. Encouraging children's creativity, they can upload their creatures to the Electropets network, adjusting growth curves.

This is a fun and interactive experience for both children and adults, bringing them together through gameplay.

## Implementation

The IoT device is currently based on the ESP32, utilizing the M5StickC Plus as the development module. The mobile app is developed using Flutter, enabling interaction with the device via Bluetooth or Wi-Fi.

An AI service is responsible for generating the creatures, hosted in the cloud. It can directly produce firmware for download to IoT devices. Data recorded during gameplay is stored either on parents' smartphones or through direct internet connectivity.


## Reference

- [Make Pixel Art in Seconds with Machine Learning](https://inikolaeva.medium.com/make-pixel-art-in-seconds-with-machine-learning-e1b1974ba572)
