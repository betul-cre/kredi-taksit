class loan():
    #interest= faiz oranı her kredi için bu oran değişir
    #e= ihtiyaç kredisi inputu
    # f= taşıt kredisi inputu
    # g= konut kredisi inputu
    # aynı şekilde sırasıyla e_b, f_b, g_b bu kredilerin borç değerleri para çekildikten sonra her kredinin borcu farklı olarak buralara atanır
    def __init__(self,total_credits=950000,e=0,f=0,g=0,interest = 0,e_b=0,f_b=0,g_b=0):
        self.total_credits=total_credits

        self.e=e
        self.f=f
        self.g=g
        self.interest = interest
        self.e_b=e_b
        self.f_b=f_b
        self.g_b=g_b
    def alpha_and_omega(self):

        print("""**************
KREDİ İŞLEMLERİ PLATFORMUNA HOŞGELDİNİZ SAYIN..
    
***************""")

        a = (input("YAŞINIZI YAZINIZ:"))
        a = int(self.check_answer(a))
        while a<18:
            print("KREDİ ÇEKMEK İÇİN YAŞINIZIN 18 İN ÜSTÜNDE OLMASI GEREKMEKTEDİR")
            a = (input("YAŞINIZI TEKRAR YAZINIZ YADA BAŞA DÖNMEK İÇİN 'q' YA BASINIZ:"))
            if a == "q":
                break
            a = int(self.check_answer(a))



        else:
            pass

            b = (input("YILLIK GELİRİNİZ MİKTARINI YAZINIZ:"))
            b = int(self.check_answer(b))
            while b < 20000:
                print("KREDİ ÇEKMEK İÇİN YILLIK GELİRİNİZİN 20000 NİN ÜTÜNDE OLMASI GEREKMEKTEDİR")
                b = (input("YILLIK GELİRİNİZ MİKTARINI TEKRAR YAZINIZ YADA KREDİ İŞLEMLERİNDEN ÇIKMAK İÇİN 'q' YA BASINIZ:"))
                if b == "q":
                    break
                b = int(self.check_answer(b))


            else:
                c = (input("KREDİ NOTUNUZU YAZINIZ:"))
                c=int(self.check_answer(c))

                while c < 799:
                    print("KREDİ ÇEKMEK İÇİN KREDİ NOTUNUZUN EN AZ 800 OLMASI GEREKLİDİR ")
                    c = (input("KREDİ NOTUNUZU TEKRAR YAZINIZ YADA BAŞA DÖNMEK İÇİN 'q' YA BASIN:"))
                    if c == "q":
                        break
                    c = int(self.check_answer(c))
                if c != "q":


                    print("""******************
1.İHTİYAÇ KREDİSİ
2.TAŞIT KREDİSİ
3.KONUT KREDİSİ
        
**********************""")


                    d=input("İSTEDİĞİNİZ KREDİ TİPİNİ SEÇİN:")
                    d=self.check_answer(d)




                    if (d == "1"):
                        month = input("KREDİYİ KAÇ AY VADELİ ALMAK İSTERSİNİZ:")
                        month = int(self.check_answer(month))
                        while month > 60:
                            print("EN FAZLA 60 AY VADELİ KREDİ ALABİLİRSİNİZ")
                            month = input("KREDİYİ KAÇ AY VADELİ ALMAK İSTEDİĞİNİZİ TEKRAR YAZIN YADA BAŞA DÖNMEK İÇİN 'q' YA BASIN:")
                            if month == "q":
                                break
                            month = int(self.check_answer(month))



                        if (month != "q"):
                            print("""**************
FAİZ ORANI SEÇTİĞİNİZ VADE İLE DOĞRU ORANTILI OLARAL ARTAR BAŞLANGIÇ ORANI 0.1 DİR
*****************
                                                                                                            """)





                            self.interest = month * 0.1
                            self.e = (input("İSTEDİĞİNİZ KREDİ MİKTARINI GİRİN:"))
                            self.e = int(self.check_answer(self.e))
                            while self.e > 50000:
                                print("EN FAZLA 50.000 TL İHTİYAÇ KREDİSİ ÇEKEBİLİRSİNİZ")
                                self.interest = month * 0.1
                                self.e = (input("İSTEDİĞİNİZ KREDİ MİKTARINI TEKRAR YAZIN YADA BAŞA DÖNMEK İÇİN 'q' YA BASIN:"))
                                self.e = int(self.check_answer(self.e))

                        if self.e !="q":

                            print("TOPLAM ÖDEYECEĞİNİZ TUTAR {}+{}X{}={} TL dir".format(self.e, self.e , self.interest / 100,self.e+self.e*self.interest/100))
                            while True:
                                    contine=input("DEVAM ETMEK İSTİYOR MUSUNUZ:")
                                    if(contine=="evet"):
                                        print("PARANIZ HESABINIZA YATIRILMIŞTIR.")
                                        self.total_credits -=self.e
                                        self.e_b=self.e+self.e*self.interest/100
                                        break
                                    elif(contine=="hayır"):
                                        print("KREDİ ÇEKME İŞLEMİNİZ İPTAL EDİLMİŞTİR")
                                        break
                                    else:
                                        print("LÜTFEN 'evet' YADA 'hayır' İLE CEVAP VERİNİZ..")
                            while True:
                                con=input("YAPMAK İSTEDİĞİNİZ BAŞKA BİR İŞLEM VAR MI:")
                                if(con=="evet"):
                                    break


                                elif(con=="hayır"):
                                    print("YİNE BEKLERİZ..")
                                    exit()
                                else:
                                    print("LÜTFEN 'evet' YADA 'hayır' İLE CEVAP VERİNİZ..")



                    elif (d == "2"):

                        month = input("KREDİYİ KAÇ AY VADELİ ALMAK İSTERSİNİZ:")
                        month = int(self.check_answer(month))
                        while month > 60:
                            print("EN FAZLA 60 AY VADELİ KREDİ ALABİLİRSİNİZ")
                            month = input("KREDİYİ KAÇ AY VADELİ ALMAK İSTEDİĞİNİZİ TEKRAR YAZIN YADA BAŞA DÖNMEK İÇİN 'q' YA BASIN:")
                            if month == "q":
                                break
                            month = int(self.check_answer(month))




                        if month != "q":
                            print("""*****************
FAİZ ORANI SEÇTİĞİNİZ VADE İLE DOĞRU ORANTILI OLARAL ARTAR BAŞLANGIÇ ORANI 0.2 DİR
***********************""")
                            self.interest = month * 0.2
                            self.f = (input("İSTEDİĞİNİZ KREDİ MİKTARINI GİRİN:"))
                            self.f = int(self.check_answer(self.f))
                            while self.f > 100000:
                                print("EN FAZLA 100.000 TL KONUT KREDİSİ ÇEKEBİLİRSİNİZ")
                                self.interest = month * 0.2
                                self.f = (input("İSTEDİĞİNİZ KREDİ MİKTARINI GİRİN:"))
                                self.f = int(self.check_answer(self.f))
                        if self.f != "q":

                            print("TOPLAM ÖDEYECEĞİNİZ TUTAR {}+{}X{}={} TL dir".format(self.f, self.f , self.interest / 100,self.f+self.f*self.interest/100))
                            while True:

                                contine = input("DEVAM ETMEK İSTİYOR MUSUNUZ:")
                                if (contine == "evet"):
                                    print("PARANIZ HESABINIZA YATIRILMIŞTIR.")
                                    self.total_credits -=self.f
                                    self.f_b +=self.f+self.f*self.interest/100
                                    break
                                elif(contine=="hayır"):
                                    print("KREDİ ÇEKME İŞLEMİNİZ İPTAL EDİLMİŞTİR")
                                    break

                                else:
                                    print("LÜTFEN 'evet' YADA 'hayır' İLE CEVAP VERİNİZ..")

                        while True:
                            con=input("YAPMAK İSTEDİĞİNİZ BAŞKA BİR İŞLEM VAR MI:")
                            if(con=="evet"):
                                break
                            elif(con=="hayır"):
                                print("YİNE BEKLERİZ..")
                                exit()
                            else:
                                print("LÜTFEN 'evet' YADA 'hayır' İLE CEVAP VERİNİZ..")


                    elif (d == "3"):

                        month = input("KREDİYİ KAÇ AY VADELİ ALMAK İSTERSİNİZ:")
                        month = int(self.check_answer(month))
                        while month > 60:
                            print("EN FAZLA 60 AY VADELİ KREDİ ALABİLİRSİNİZ")
                            month = input("KREDİYİ KAÇ AY VADELİ ALMAK İSTEDİĞİNİZİ TEKRAR YAZIN YADA BAŞA DÖNMEK İÇİN 'q' YA BASIN:")
                            if month == "q":
                                break
                            month = int(self.check_answer(month))


                        if month != "q":
                            print("""***************
FAİZ ORANI SEÇTİĞİNİZ VADE İLE DOĞRU ORANTILI OLARAL ARTAR BAŞLANGIÇ ORANI 0.3 DİR
*****************""")

                            self.interest = month * 0.3
                            self.g = (input("İSTEDİĞİNİZ KREDİ MİKTARINI GİRİN:"))
                            self.g=int(self.check_answer(self.g))
                            while self.g > 15000:
                                print("EN FAZLA 150.000 TL KONUT KREDİSİ ÇEKEBİLİRSİNİZ")
                                self.interest = month * 0.3
                                self.g = (input("İSTEDİĞİNİZ KREDİ MİKTARINI TEKRAR YAZIN YADA BAŞA DÖNMEK İÇİN 'q' YA BASIN :"))
                                self.g = int(self.check_answer(self.g))

                            if self.g != "q":
                                print("TOPLAM ÖDEYECEĞİNİZ TUTAR {}+{}X{}={} TL dir".format(self.g, self.g , self.interest / 100,self.g+self.g*self.interest/100))
                                while True:
                                    contine = input("DEVAM ETMEK İSTİYOR MUSUNUZ:")
                                    if (contine == "evet"):
                                        print("PARANIZ HESABINIZA YATIRILMIŞTIR.")
                                        self.total_credits -=self.g
                                        self.g_b +=self.g+self.g*self.interest/100
                                        break
                                    elif(contine=="hayır"):
                                        print("KREDİ ÇEKME İŞLEMİNİZ İPTAL EDİLMİŞTİR")
                                        break
                                    else:
                                        print("LÜTFEN 'evet' YADA 'hayır' İLE CEVAP VERİNİZ..")
                                while True:

                                        con=input("YAPMAK İSTEDİĞİNİZ BAŞKA BİR İŞLEM VAR MI:")
                                        if(con=="evet"):
                                            break
                                        elif(con=="hayır"):
                                            print("YİNE BEKLERİZ..")
                                            exit()
                                        else:
                                            print("LÜTFEN 'evet' YADA 'hayır' İLE CEVAP VERİNİZ..")
                    else:
                        print("LÜTFEN GEÇERLİ BİR İŞLEM SEÇİN")

# eğer hiç kredi çekmeden taksit ödemeye gelirsen borç değerleri olan(e_b, f_b, g_b)= 0 olduğu için herhangi bir borcunuz yoktur uyarısı alırsın
    def instalment(self):

            print("""******************
1.İHTİYAÇ KREDİSİ
2.TAŞIT KREDİSİ
3.KONUT KREDİSİ
*******************""")

            pnl=input("ÖDEMEK İSTEDİĞİNİZ KREDİ TİPİNİ SEÇİNİZ:")
            if(pnl=="1"):
                    if(self.e_b==0):
                        print("HERHANGİ BİR BORCUNUZ YOK")
                        pass
                    else:
                        #debt= ödemek istediğin borcun tutarının inputu ve bu tutar borcun hangi kısımdaysa yani e_b yada f_b gibi farklı yerlerde olabilir seçtiğin krediye bağlı olarak ordan eksiltilir
                        # ve ödediğin tutar olan debt bankanın toplam kredi miktarına eklenir
                        debt=(input("ÖDEMEK İSTEDİĞİNİZ TUTARI YAZIN:"))
                        debt=int(self.check_answer(debt))
                        while debt > self.e_b:
                            print("ÖDEMEK İSTEDİĞİNİZ TUTAR BORCUNUZDAN FAZLA TEKRAR DENEYİN.")
                            debt = (input("ÖDEMEK İSTEDİĞİNİZ TUTARI YAZIN:"))
                            debt = int(self.check_answer(debt))
                        if debt <= self.e_b:
                            self.total_credits +=debt
                            self.e_b -=debt
                        print("KALAN BORCUNUZ {} TL".format(self.e_b))
                        while True:
                            con=input("YAPMAK İSTEDİĞİNİZ BAŞKA BİR İŞLEM VAR MI:")
                            if(con=="evet"):
                                break
                            elif(con=="hayır"):
                                print("YİNE BEKLERİZ..")
                                exit()
                            else:
                                print("LÜTFEN 'evet' YADA 'hayır' İLE CEVAP VERİNİZ..")


            elif(pnl=="2"):
                    if (self.f_b ==0):
                        print("HERHANGİ BİR BORCUNUZ YOK")
                        pass
                    else:

                        debt=(input("ÖDEMEK İSTEDİĞİNİZ TUTARI YAZIN:"))
                        debt = int(self.check_answer(debt))
                        while debt > self.f_b:
                            print("ÖDEMEK İSTEDİĞİNİZ TUTAR BORCUNUZDAN FAZLA TEKRAR DENEYİN.")
                            debt = (input("ÖDEMEK İSTEDİĞİNİZ TUTARI YAZIN:"))
                            debt = int(self.check_answer(debt))

                        if debt <= self.f_b:
                            self.total_credits +=debt
                            self.f_b -=debt
                        print("KALAN BORCUNUZ {} TL".format(self.f_b))
                        while True:
                            con=input("YAPMAK İSTEDİĞİNİZ BAŞKA BiR İŞLEM VAR MI:")
                            if(con=="evet"):
                                break
                            elif(con=="hayır"):
                                print("YİNE BEKLERİZ..")
                                exit()
                            else:
                                print("LÜTFEN 'evet' YADA 'hayır' İLE CEVAP VERİNİZ..")

            elif(pnl=="3"):
                    if(self.g_b==0):
                        print("HERHANGİ BİR BORCUNUZ YOK")
                        pass
                    else:
                        debt=(input("ÖDEMEK İSTEDİĞİNİZ TUTARI YAZIN:"))
                        debt=int(self.check_answer(debt))
                        while debt > self.g_b:
                            print("ÖDEMEK İSTEDİĞİNİZ TUTAR BORCUNUZDAN FAZLA TEKRAR DENEYİN.")
                            debt = (input("ÖDEMEK İSTEDİĞİNİZ TUTARI YAZIN:"))
                            debt = int(self.check_answer(debt))
                        if debt <= self.g_b:
                            self.total_credits +=debt
                            self.g_b -=debt
                        print("KALAN BORCUNUZ {} TL".format(self.g_b))
                        while True:
                            con=input("YAPMAK İSTEDİĞİNİZ BAŞKA BİR İŞLEM VAR MI:")
                            if(con=="evet"):
                                break
                            elif(con=="hayır"):
                                print("YİNE BEKLERİZ..")
                                exit()
                            else:
                                print("LÜTFEN 'evet' YADA 'hayır' İLE CEVAP VERİNİZ..")


    # adamın girdiği değerlerin rakam olup olmadığını kontrol eden fonksiyon ,yukarda değeri int olan inputları altında görersin
    def check_answer(self,answer):
        while True:
            try:
                x=int(answer)
                return answer
            except:
                answer = input("LÜTFEN RAKAM GİRİNİZ:")




x = loan()
while True:
    print("""*****************
BANKAMIZA HOŞGELDİNİZ
1.KREDİ ÇEKME
2.TAKSİT ÖDEME
******************""")

    task = input("YAPMAK İSTEDİĞİNİZ EYLEMİ SEÇİNİZ:")


    if task == "1":
        x.alpha_and_omega()


    elif task == "2":
        print("TAKSİT ÖDEME İŞLEMLERİNE HOŞGELDİNİZ SAYIN..")
        x.instalment()
    else:
        print("LÜTFEN GEÇERLİ BİR İŞLEM SEÇİN")





