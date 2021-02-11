
# Snake Zizare Jokoa  


Programatu dudan jokoa snake motakoa da  (ikus Snake_video_game_genre).

 

Snake joko mota hori ez dut nik asmatu, 1970 urtean sortu zen. Jokoan “W,A,S,D” teklak erabiliz “suge” bat mugitzen duzu. Sugea luzeagoa egiten da  janaria lortzen duenean, eta horma bat ukitzean edo bere burua ukitzean hil egiten da. Jokoaren helburua janari asko lortzea da, baina janari gehiago lortzean sugea luzeago bihurtzen da eta zailagoa da bere burua ez ukitzea. Gero eta janari gehiago lortu,  gero eta puntu gehiago.



Jokoa zabaltzean menu bat dago non jokoaren tamaina, abiadura aldatzeko, eta puntuazio hoberenak ikusteko botoiak daude. Abiaduran eta tamaina n 3 aukera eskaintzen dira. Azkenik, jolasten hasteko beste botoi bat dago. Jokoa hastean sugearen luzera 2koa da, hau da, bi karratuko tamaina dauka. Gainera, ausaz aukeratutako toki batean janaria agertuko da. Sugea berehala mugitzen hasten da. W sakatzen baduzu sugea gora mugituko da, D sakatzen baduzu eskuinera, S sakatzen behera eta A sakatzen ezkerrera.

 

### Datuen errepresentazioa. Hasierako egoera

 

Jokoa inplementatzeko, zenbakiz osatutako matrize handi bat erabili dut non janaria 1 zenbakia da, sugearen burua 2 zenbakia eta sugearen gorpua 2 tik gorako zenbakiak (2-3-4-5-6...) . Beste gelaxka guztietan 0 zenbakia dago.

 ![1](https://user-images.githubusercontent.com/74160112/107695325-b7e1bb00-6cb0-11eb-8da2-692fdbb83de2.PNG)

### Mugimendua

 

Ondoren, jokoa hasten denean, sugearen mugimenduko urrats bakoitzean 2 edo handiagoak diren zenbaki guztiei (sugea horietan dago) bat zenbakia gehitzen zaie baita “mod(sugearen luzera +2)” eragiketa ere aplikatu gero. Horrela gorputzaren azken zatiaren gelaxkan  “+1 mod(sugearen luzera +2)” egitean 0 zenbakia geratuko da, hau da, hutsik geratuko da gelaxka, nah dugun bezala. Ondoren, azken ukitutako teklaren arabera, burua mugituko da (2 zenbakia jartzea gelaxka berri batean).

 

Mugituko den gelaxkan 0 edo 1 badago toki horretan 2 jarriko da eta lehenago burua zen gelaxkan  orain 3 zenbakia egongo da +1 egin baita, eta ondorioz orain gorputzaren zati bat da. Burua sortu den gelaxkan lehen 1 zenbakia (janaria) bazegoen, orduan sugearen luzera handitu egingo da (+1)  eta janaria jarri beharko da beste gelaxka batean (1 zenbakia).

 

Beste kasuetan sugea hil egiten da. Adibidez, sugearen luzera 4 bada eta azken ukitutako
tekla W bada, hau da, gorako norabideko tekla, honakoa gertatuko da:

Hasierako egoera:

![2](https://user-images.githubusercontent.com/74160112/107695327-b7e1bb00-6cb0-11eb-97c8-e794d8119f63.PNG)

Sugearen gorpuari, burua ez dena, bat gehitu eta 6-ren modulua (6 = luzera + 2) egin ondoren:

![3](https://user-images.githubusercontent.com/74160112/107695329-b7e1bb00-6cb0-11eb-8edd-02737545f757.PNG)

Buru berria sortu (2) eta janari berria sortu (1) ondoren:

![4](https://user-images.githubusercontent.com/74160112/107695330-b87a5180-6cb0-11eb-9c3b-ff196b8d58fa.PNG)

Bukaerako egoera, luzera bat handiagoa denez mod 7 egiten da eta horrela sugea luzeagoa da:

![5](https://user-images.githubusercontent.com/74160112/107695331-b87a5180-6cb0-11eb-9bad-819c62fb9678.PNG)

 

### Jokoa bistaratzen

Jokoa funtzionatzen dagoenean matrizea irudikatu egiten da urrats bakoitzean. Hasieran dena beltzean jarri, ondoren 1 jartzen duen tokietan (janaria) karratu berde bat sortu, eta beste zenbaki guztietan karratu zuriak sortu.

![6](https://user-images.githubusercontent.com/74160112/107695315-b57f6100-6cb0-11eb-97de-33d5d5244816.PNG)

Mugimendua egoteko while begizta bat erabiltzen da eta while-ko iterazio bakoitzean pantailan agertzen dena berriro irudikatu.


Jokoaren mugimendua motelago joatea nahi bada egin behar den bakarra itxaroteko while exekuzio batzuk jartzea da. Horretarako aldagai bat definitu dut while bakoitzean inkrementatu  (+1) egiten dena eta aldagaiaren balioa 20ren multiploa den bakoitzean pantaila irudikatzen da. Abiadura aldatzeko egin behar den bakarra 20 hori duen aldagaiaren balioa aldatzea da.


Jokalariak lortzen dituen puntuazioa sugearen azken luzera -2 izaten da.

![7](https://user-images.githubusercontent.com/74160112/107695319-b617f780-6cb0-11eb-80e5-cfa927ddfd42.PNG)

Sugea hiltzen denean puntuazioa gordetzeko aukera dago eta ondoren puntuazioen lista bat ikus daiteke.

![8](https://user-images.githubusercontent.com/74160112/107695320-b6b08e00-6cb0-11eb-85a5-d86bf79e1834.PNG)

Puntuazioa gordetzean izena ere jarri daiteke.

![9](https://user-images.githubusercontent.com/74160112/107695321-b6b08e00-6cb0-11eb-8112-be985ae9bea9.PNG)

Jokuaren datuak erakusterakoan lortutako puntuak, jokalariaren izena, sugearen abiadura eta tamaina agertzen dira, eta datu gehiago sartzean beti ordenatuta agertzen dira. Datuak gordetzeko dokumentu bat sortzen da bektore batekin.

![10](https://user-images.githubusercontent.com/74160112/107695323-b7492480-6cb0-11eb-83d9-08d65a4539f8.PNG)

![11](https://user-images.githubusercontent.com/74160112/107695324-b7492480-6cb0-11eb-8aac-ad9a04b73edd.PNG)

### Laburpena eta ondorioak

Laburbiltzeko, Snake-Zizare jokoa egiteko matrize bat erabili dut zenbakiekin osatuta eta jokoaren martxa kontrolatzeko kalkulu guztiak matrizean egin ditut. Urratsa bakoitzaren ondoren matrizeko zenbaki guztiak pantailan irudikatu ditut kolorezko karratuak erabiliz.


Ondorioz, gelan ikasitakoa erabilgarria da, adibidez matrizeak, bektoreak edo beste dokumentu bateko datuak idaztea eta irakurtzea. Baina ez da bakarrik erabilgarria oinarrizko programazioan ikasitakoa, matematika diskretuan ikasitako aljebra modularra ere erabilgarria da jokoak eta bestelako aplikazioak programatzean.
