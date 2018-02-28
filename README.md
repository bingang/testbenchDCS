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
           說明:把docker-compose.yml這個檔案裏面的image build起來，但沒執行裡面的container
Sudo docker swarm init  --addvertise-addr <manager的IP>  
Sudo docker swarm join –token <步驟4的output> 
          說明 : 在除了manager的每台主機上都做一次
sudo docker network create --driver overlay BitcoinNetworkName 
          說明 : 最後一個為網路的名稱
cd workspace
./masternodecreate.sh
./clientnodecreate.sh    
         說明 : 會詢問需要幾個node( = container數目),輸入需要的數字





