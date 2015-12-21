# Initialize a digitalocean droplet with a MongoDB + Ubuntu 14.04 image

# Login and change password
ssh root@46.101.234.224

# Add a new user "max" and give him a password
adduser max
# Give "max" sudo rights
gpasswd -a max sudo

# Change "PermitRootLogin yes" to "PermitRootLogin no"
nano /etc/ssh/sshd_config

# Restart SSH
service ssh restart

# Switch to user "max"
sudo su max

# Configure the timezone
sudo dpkg-reconfigure tzdata
# Configure NTP Synchronization
sudo apt-get update
sudo apt-get install ntp
# Create a Swap File
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
sudo sh -c 'echo "/swapfile none swap sw 0 0" >> /etc/fstab'

# Setup Python and Apache
sudo apt-get update
sudo apt-get install apache2
sudo apt-get install python3-pip python3-dev libapache2-mod-wsgi-py3

# Clone the repository containing the code
cd /var/www
sudo apt-get install git
sudo git clone https://github.com/MaxHalford/OpenBikes
sudo chmod -R 777 OpenBikes/
cd OpenBikes

# Install the necessary Python libraries (takes some time)
sudo apt-get install libblas-dev liblapack-dev libatlas-base-dev gfortran
sudo apt-get install python3-lxml
sudo pip3 install -r setup/requirements.txt

# Add the cities
cd setup
sudo ./refresh_cities.sh
cd ..

# Create the upstart script to collect data
sudo cp setup/scripts/ob-collect.conf /etc/init/
# Start it
sudo start ob-collect

# Create the upstart script to train predictors
sudo cp setup/scripts/ob-learn.conf /etc/init/
# Start it
sudo start ob-learn

# Create the upstart script to restart the robots
sudo cp setup/scripts/ob-restart.conf /etc/init/
# Start it
sudo start ob-restart

# Configure and enable a virtual host
sudo cp setup/scripts/OpenBikes.conf /etc/apache2/sites-available/
sudo a2ensite OpenBikes
sudo service apache2 reload
sudo service apache2 restart

# Reboot the server and you should be done!
sudo reboot