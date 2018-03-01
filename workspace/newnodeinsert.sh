sudo docker network inspect BitcoinNetworkName | grep 'IPv4Address' | head -n 1 | awk -F'"' '{print $4}' | awk -F'/' '{print $1}' > info/trade0/central.txt
python InsertNode.py
sudo docker stack deploy -c docker-compose2.yml mybitcoin
