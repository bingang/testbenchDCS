# BitcoinCompose
Bitcoin in Docker-Compose
=========================
Try to use dockercompose to create a lot of bitcoin node   
We use bitcoincore v0.14rc3  
Usage:   
------
git clone https://github.com/bingang/testbenchDCS  
cd testbenchDCS  
sudo docker build BitcoinDev -t bitcoindev  
sudo docker-compose build  
Sudo docker swarm init  --addvertise-addr <manager的IP>    
Sudo docker swarm join –token <步驟4的output>  
sudo docker network create --driver overlay BitcoinNetworkName   
cd workspace  
./masternodecreate.sh  
./clientnodecreate.sh    






