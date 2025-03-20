#!/bin/bash
sudo apt-get install cowsay -y

cowsay -f dragon "Run for the cover, i am a dragon ....RAWR" >> dragon.txt

grep -i "dragon" dragon.txt

cat dragon.txt

ls -lrta
