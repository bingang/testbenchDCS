import uuid
import os
print "Insert how many node you want to insert"
NumOfInsertNode = input()
print "Create "+str(NumOfInsertNode)+" node"
datadir=os.getcwd()
with open("docker-compose2.yml", "w") as myfile:
    myfile.write("version: '3'")
    myfile.write("\n")
    myfile.write("services:")
    myfile.write("\n")
    NumExistingNode =  ?? #get form somewhere
    i = NumExistingNode
    while i < NumOfInsertNode + NumExistingNode:
	os.system('sudo rm -r '+str(datadir)+'/info/trade'+str(i+1))
	os.system('mkdir '+str(datadir)+'/info/trade'+str(i+1))
	os.system('echo "rpcuser=Node'+str(i+1)+'\nrpcpassword=Node'+str(i+1)+'\nrpcallowip=0.0.0.0/0\n" > '+str(datadir)+'/info/trade'+str(i+1)+'/bitcoin.conf')
	os.system('cp info/trade0/central.txt info/trade'+str(i+1)+'/central.txt')
        portsNumber = 20001+i
	backupport = 25001+i
        nodeName = uuid.uuid4()
        print "Node Name: "+str(nodeName)
        myfile.write(" "+str(nodeName)+":")
        myfile.write("\n")
        myfile.write("  image: bitcoinnode")
        myfile.write("\n")
        myfile.write("  ports:")
        myfile.write("\n")
        myfile.write("   - "+str(portsNumber)+":18332")
	myfile.write("\n")
        myfile.write("   - "+str(backupport)+":18333")
	#+str(portsNumber)
        myfile.write("\n")
	myfile.write("  networks:")
	myfile.write("\n")
	myfile.write("   - mybitcoinnetwork")
	myfile.write("\n")
	myfile.write("  deploy:")
	myfile.write("\n")
	myfile.write("   restart_policy:")
        myfile.write("\n")
	myfile.write("     condition: on-failure")
	myfile.write("\n")
	myfile.write("  volumes:")
        myfile.write("\n")
        myfile.write("   - "+str(datadir)+"/info/trade"+str(i+1)+":/root/.bitcoin")
        myfile.write("\n");
	#myfile.write("  depends_on:")
        #myfile.write("\n")
        #myfile.write("   - a")
        myfile.write("\n")
	i+=1
    myfile.write("networks:")
    myfile.write("\n")
    myfile.write(" mybitcoinnetwork:")
    myfile.write("\n")
    myfile.write("  external:")
    myfile.write("\n")
    myfile.write("    name: BitcoinNetworkName")
    myfile.write("\n")
print "Create Done "
