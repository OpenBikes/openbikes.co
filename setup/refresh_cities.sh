################
### JCDecaux ###
################

mkdir common/metadata/
mkdir app/static/geojson/
mkdir common/regressors

echo "{}" > common/metadata/centers.json
echo "{}" > common/metadata/cities.json
echo "{}" > common/metadata/names.json
echo "{}" > common/metadata/predictions.json
echo "{}" > common/metadata/providers.json
echo "{}" > common/metadata/updates.json
echo "{}" > common/metadata/stations.json
echo "{}" > common/metadata/owm.json

python3 remove.py jcdecaux Amiens France
python3 add.py jcdecaux Amiens Amiens "Amiens, FR" France France Yes

python3 remove.py jcdecaux Bruxelles-Capitale Belgium
python3 add.py jcdecaux Bruxelles-Capitale Bruxelles "Brussels, BE" Belgium Belgique Yes

python3 remove.py jcdecaux Besancon France
python3 add.py jcdecaux Besancon Besancon "Besancon, FR" France France Yes

python3 remove.py jcdecaux Cergy-Pontoise France
python3 add.py jcdecaux Cergy-Pontoise Cergy "Cergy, FR" France France Yes

python3 remove.py jcdecaux Creteil France
python3 add.py jcdecaux Creteil Créteil "Creteil, FR" France France Yes

python3 remove.py jcdecaux Dublin Irlande
python3 add.py jcdecaux Dublin Dublin "Dublin, IE" Irlande Irlande Yes

python3 remove.py jcdecaux Goteborg Sweden
python3 add.py jcdecaux Goteborg Göteborgs "Gothenburg, Sweden" Sweden Sverige Yes

python3 remove.py jcdecaux Kazan Russia
python3 add.py jcdecaux Kazan Казан "Kazan, RU" Russia Россия Yes

python3 remove.py jcdecaux Lillestrom Norway
python3 add.py jcdecaux Lillestrom Lillestrøm "Skedsmo, Norway" Norway Norge Yes

python3 remove.py jcdecaux Ljubljana Slovenia
python3 add.py jcdecaux Ljubljana Laibach "Ljubljana, SI" Slovenia Slovenija Yes

python3 remove.py jcdecaux Lund Suède
python3 add.py jcdecaux Lund Lund "Lund, SE" Sweden Sverige Yes

python3 remove.py jcdecaux Luxembourg Luxembourg
python3 add.py jcdecaux Luxembourg Lëtzebuerg "Luxembourg, LU" Luxembourg Lëtzebuerg Yes

python3 remove.py jcdecaux Lyon France
python3 add.py jcdecaux Lyon Lyon "Lyon, FR" France France Yes

python3 remove.py jcdecaux Marseille France
python3 add.py jcdecaux Marseille Marseille "Marseille, FR" France France Yes

python3 remove.py jcdecaux Mulhouse France
python3 add.py jcdecaux Mulhouse Mulhouse "Mulhouse, FR" France France Yes

python3 remove.py jcdecaux Namur Belgium
python3 add.py jcdecaux Namur Namur "Namur, BE" Belgium Belgique Yes

python3 remove.py jcdecaux Nancy France
python3 add.py jcdecaux Nancy Nancy "Nancy, FR" France France Yes

python3 remove.py jcdecaux Nantes France
python3 add.py jcdecaux Nantes Nantes "Nantes, FR" France France Yes

python3 remove.py jcdecaux Paris France
python3 add.py jcdecaux Paris Paris "Paris, FR" France France Yes

python3 remove.py jcdecaux Rouen France
python3 add.py jcdecaux Rouen Rouen "Rouen, FR" France France Yes

python3 remove.py jcdecaux Seville Spain
python3 add.py jcdecaux Seville Sevilla "Seville, Spain" Spain España Yes

python3 remove.py jcdecaux Stockholm Sweden
python3 add.py jcdecaux Stockholm Stockholm "Stockholm, SE" Sweden Sverige Yes

python3 remove.py jcdecaux Toulouse France
python3 add.py jcdecaux Toulouse Toulouse "Toulouse, FR" France France Yes

python3 remove.py jcdecaux Toyama Japan
python3 add.py jcdecaux Toyama "Toyama - 富山" "Toyama-shi, JP" Japan "Nihon - 日本" Yes

python3 remove.py jcdecaux Valence Spain
python3 add.py jcdecaux Valence Valencia "Valencia, ES" Spain España Yes

python3 remove.py jcdecaux Vilnius Lithania
python3 add.py jcdecaux Vilnius Vilnius "Vilnius, LT" Lithuania Lietuva Yes

#################
### Citi Bike ###
#################

python3 remove.py citibike New-York USA
python3 add.py citibike New-York New-York "New York, United States of America" USA USA Yes

#########################
### Capital Bikeshare ###
#########################

python3 remove.py capitalbikeshare Washington-DC USA
python3 add.py capitalbikeshare Washington-DC "Washington DC" "Washington, United States of America" USA USA Yes

##############
### Hubway ###
##############

python3 remove.py hubway Boston USA
python3 add.py hubway Boston Boston "Boston, US" USA USA Yes

################
### Niceride ###
################

python3 remove.py niceride Minneapolis USA
python3 add.py niceride Minneapolis Minneapolis "Minneapolis, US" USA USA Yes

############
### Bixi ###
############

#python3 remove.py bixi Toronto Canada
#python3 add.py bixi Toronto Toronto "Toronto, CA" Canada Canada No

#python3 remove.py bixi Ottawa Canada
#python3 add.py bixi Ottawa Ottawa "Ottawa, CA" Canada Canada No

#python3 remove.py bixi Montreal Canada
#python3 add.py bixi Montreal Montréal "Montreal, CA" Canada Canada No

##############
### Keolis ###
##############

python3 remove.py keolis Rennes France
python3 add.py keolis Rennes Rennes "Rennes, FR" France France Yes

#################
### Machikado ###
#################

python3 remove.py machikado Kyoto-Minaport Japan
python3 add.py machikado Kyoto-Minaport "Kyōto - 京都" "Kyoto, JP" Japan "Nihon - 日本" Yes

#############
### Divvy ###
#############

python3 remove.py divvy Chicago USA
python3 add.py divvy Chicago Chicago "Chicago, US" USA USA No

################
### Bay area ###
################

python3 remove.py bayarea Bay-Area USA
python3 add.py bayarea Bay-Area "Bay Area" "Foster City, US" USA USA No

#######################
### Bikechatannooga ###
#######################

python3 remove.py bikechattanooga Chattanooga USA
python3 add.py bikechattanooga Chattanooga Chattanooga "Chattanooga, US" USA USA No

#################
### Santander ###
#################

python3 remove.py santander London UK
python3 add.py santander London London "London, GB" UK UK No

####################
### Citybikewien ###
####################

python3 remove.py citybikewien Vienna Austria
python3 add.py citybikewien Vienna Wien "Vienna, AT" Austria Österreich No

###############
### Velocea ###
###############

python3 remove.py velocea Vannes France
python3 add.py velocea Vannes Vannes "Vannes, FR" France France No

################
### Velobleu ###
################

python3 remove.py velobleu Nice France
python3 add.py velobleu Nice Nice "Nice, FR" France France No

##############
### Velin  ###
##############

python3 remove.py velin Calais France
python3 add.py velin Calais Calais "Calais, FR" France France No

################
### Clivelo  ###
################

python3 remove.py clivelo Montpellier France
python3 add.py clivelo Montpellier Montpellier "Montpellier, FR" France France No

################
### Velopop  ###
################

python3 remove.py velopop Avignon France
python3 add.py velopop Avignon Avignon "Avignon, FR" France France No

###################
### Velolibelo  ###
###################

python3 remove.py velolibelo Valence France
python3 add.py velolibelo Valence Valence "Valencia, ES" France France No

###############
### Velhop  ###
###############

python3 remove.py velhop Strasbourg France
python3 add.py velhop Strasbourg Strasbourg "Strasbourg, FR" France France No

################
### Velivert ###
################

python3 remove.py velivert Saint-Etienne France
python3 add.py velivert Saint-Etienne Saint-Etienne "Saint-Etienne, FR" France France No

#############
### Tashu ###
#############

python3 remove.py tashu Daejeon South-Korea
python3 add.py tashu Daejeon "Daejeon - 대전" "Daejeon, KR" South-Korea "South-Korea - 대한민국" No

################
### Decobike ###
################

python3 remove.py decobike Miami-Beach USA
python3 add.py decobike Miami-Beach Miami-Beach "Miami Beach, United States of America" USA USA No

################
### Nextbike ###
################

python3 remove.py nextbike Warsaw Poland
python3 add.py nextbike Warszawa Warszawa "Warsaw, Poland" Poland Poland No

python3 remove.py nextbike Riga Latvia
python3 add.py nextbike Riga Riga "Riga, LV" Latvia Latvia No

python3 remove.py nextbike Jurmala Latvia
python3 add.py nextbike Jurmala Jurmala "Jurmala, LV" Latvia Latvia No

python3 remove.py nextbike Wroclaw Poland
python3 add.py nextbike Wroclaw "Wrocław" "Wroclaw, PL" Poland Poland No

python3 remove.py nextbike Seferihisar Turkey
python3 add.py nextbike Seferihisar Seferihisar "Seferihisar, TR" Turkey Turkey No

python3 remove.py nextbike Dubai UnitedArabEmirates
python3 add.py nextbike Dubai Dubai "Dubai, AE" UnitedArabEmirates "United Arab Emirates" No

python3 remove.py nextbike AbuDhabi UnitedArabEmirates
python3 add.py nextbike AbuDhabi "Abu Dhabi" "Abu Dhabi, United Arab Emirates" UnitedArabEmirates "United Arab Emirates" No

python3 remove.py nextbike Zagreb Croatia
python3 add.py nextbike Zagreb Zagreb "Zagreb - Centar, HR" Croatia Croatia No

python3 remove.py nextbike Krakow Poland
python3 add.py nextbike Krakow "Kraków" "Krakow, PL" Poland Poland No

python3 remove.py nextbike Bialystok Poland
python3 add.py nextbike Bialystok "Białystok" "Bialystok, PL" Poland Poland No

python3 remove.py nextbike Belfast UK
python3 add.py nextbike Belfast Belfast "Belfast, GB" UK UK No

python3 remove.py nextbike KonstancinJeziorna Poland
python3 add.py nextbike KonstancinJeziorna "Konstancin-Jeziorna" "Konstancin-Jeziorna, Poland" Poland Poland No

python3 remove.py nextbike Sibenik Croatia
python3 add.py nextbike Sibenik "Šibenik" "Sibenik, HR" Croatia Croatia No

python3 remove.py nextbike Lublin Poland
python3 add.py nextbike Lublin Lublin "Lublin, PL" Poland Poland No

python3 remove.py nextbike GrodziskMazowiecki Poland
python3 add.py nextbike GrodziskMazowiecki "Grodzisk Mazowiecki" "Grodzisk Mazowiecki, Poland" Poland Poland No

python3 remove.py nextbike Pittsburgh USA
python3 add.py nextbike Pittsburgh Pittsburgh "Pittsburgh, US" USA USA No

python3 remove.py nextbike Heidelberg Germany
python3 add.py nextbike Heidelberg Heidelberg "Heidelberg, DE" Germany Germany No

python3 remove.py nextbike WestPalmBeachFlorida USA
python3 add.py nextbike WestPalmBeachFlorida "West Palm Beach Florida" "West Palm Beach, United States of America" USA USA No

python3 remove.py nextbike Auckland NewZealand
python3 add.py nextbike Auckland Auckland "Auckland, NZ" NewZealand "New Zealand" No

python3 remove.py nextbike Christchurch NewZealand
python3 add.py nextbike Christchurch Christchurch "Christchurch, NZ" NewZealand "New Zealand" No
