from typing import List


class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        d = dict()
        for mapping in mappings:
            if mapping[0] in d.keys():
                d[mapping[0]] += mapping[1]
            else:
                d[mapping[0]] = mapping[1]
        length = len(sub)
        starts = sub[0] + d.get(sub[0], "")
        s_index = []
        for start in starts:
            for i in range(len(s)):
                if s[i] == start:
                    s_index.append(i)
        candidates = []
        for start in s_index:
            cur = s[start: start + length]
            if len(cur) == length:
                candidates.append(cur)
        for candidate in candidates:
            candidate = list(candidate)
            temp = list(sub)
            for i in range(length):
                ch1 = candidate[i]
                ch2 = sub[i]
                if ch1 != ch2:
                    if ch1 in d.get(ch2, ch2):
                        temp[i] = ch1
            if candidate == temp:
                return True
        return False


if __name__ == '__main__':
    s = "27awmey8ooynp9usl9q2gg2co2eclhw3wk2uwje4m4tp71qr5s9xrieroj12hy4l6jfx01oxekipt96vqpjbfl4v686mdppgo722y1r6jk0iaeq1nd7tq1s8hr4pk0z906ntxyjtqgyzfbxmkp63x970sbjezlnvwj37bdkrrxth2x7z30oazq8dnq103ntswp2nzeef8rj89kd0it9mlj3pyw5qpggcdmsg49nz55gik6yavx2nrqt8m23i5r3p3b7nb6h46z2xbq2qrp9xo60uqioz02d54roqka2fzhk0kh4pnaofvbz"
    sub = "ibhqq947tqqsdur0pk9r906ngxyjtqgyzzyxm6pf3l9k9nylhzl9q2l37ydkrrlthcl7z39obzqd4nqq939gnwpc9zhefdrldfkd0itfmxj3py29qpygl4msy"
    mappings = [["c", "2"], ["a", "h"], ["j", "h"], ["q", "1"], ["l", "5"], ["f", "9"], ["x", "l"], ["r", "z"], ["b", "0"],
     ["b", "c"], ["1", "5"], ["e", "6"], ["v", "8"], ["h", "u"], ["n", "i"], ["a", "7"], ["g", "j"], ["c", "b"],
     ["n", "e"], ["f", "u"], ["j", "5"], ["9", "n"], ["q", "w"], ["x", "k"], ["e", "j"], ["5", "t"], ["2", "w"],
     ["v", "0"], ["m", "a"], ["3", "e"], ["k", "7"], ["j", "e"], ["y", "g"], ["8", "o"], ["w", "v"], ["5", "m"],
     ["5", "8"], ["0", "x"], ["y", "b"], ["q", "v"], ["h", "e"], ["8", "c"], ["f", "6"], ["b", "a"], ["d", "8"],
     ["u", "f"], ["l", "x"], ["l", "c"], ["u", "i"], ["6", "k"], ["n", "s"], ["9", "5"], ["z", "f"], ["g", "t"],
     ["4", "d"], ["0", "4"], ["l", "j"], ["u", "h"], ["9", "0"]]
    # s = "r8n0mtojdlseusta8r6ch97s30px4o0uy7dpqerclo5smb1uk6wrw0i50gvhj9mgw75kgr5cn91m4j76ohav85b0g0fusdk0adacr6lva18uerzc0568uknmyuejj3pmv41kmlcdrdqgx0ziohvsq61c287y67y9kxzhs95e8f5xn8b9ddg76btpyjqyd2uaxlo4ki1jhitt1jkyfhfcevaqnxe9i944dqa1p41gh2pzphmsk6bhav7mggjlmhtxwny0gabec8o26mofxycpud6wlsxf39kddmz7cl59fzcfa0xahqklguuuz8smuewmz100nuxgu4882xml8tnkzzyy1xlxwhw1tz7dgrdkkop3iovzxlvsgobctxpcn2vdmxts825ls2izza7c3ugo8fogoot2ttiovsn5h9enu8gww9upltwhfiyf91h0jaztngtooan4394o79qn47zeq0ifz7z1r8igfwc41vsw19uxjljh29f2icgr9z1hxm92pje6rsfz9gkrwib2tmpvlksfjdbwzif0yfe24quu24o1sp29mhhxc9zd1e6avu6cdsgc5qxeff63td4aagjj7cjppwnsrcxjz418vhzroj936u0af2aops5t3q5abw5i6n2r9no6wyrg59mv9ww6s1qzru974vgg790n906kvbws2j0jthlrdwu8kjx01ny6ae5jzeo8ebe4g0ei07t41haoeomr26epdc9kudhqgd6q2yyq8ffrisw08076w11bo7yk1pf3qppfgbcenmwzib4xb05tw6whv19chaftn5z5gsnogh9sdal8gkitrk3f5wy2fnq9nnbtfbogecr61frzt7jon23kay6ilh0re87eiqlawmishgn7qdjmilyxyne088i2o54121qq71qjbqxqsgbaj7ep2rs5b356dfrz71g93cz9aipm8sau8kk1ysysnzqy6aw26brgysrv16ccw135wwqfsaoox4hvtf05z4wpgf6njcxzql2f1m8au1slsowwzfr5mlg3sj8tnwjiw4m46cka17yk7j8wvpqiria6xphgvp0unybdlh0e0m0efn7icumzphlm8a9qvgolsgsqtakmsw9v0pg2kog6j9ad55fgr4cjbg9ok8kvtgxkp0yop55v2ujnc2muzpiuf61n6ga5ygm9tawapd8hh4icriu96zdp43gxj0qn3wwtb0k4vyxok2tpf5vk6kp8l3ihdo9yd5hrjpghyfrqp32k3mttghzch06z18gytjegz4r4x6m01ixnznef2689hamgmklb40akp7tevw181t8xzhsjovx83bkbdiy45t17k4obwbs3iqginwg6n6i9dsk7t0hz5o6jo11s7jputm3rb51yiyy1rye3lv1ncfkv83h11syzi4bw61n1zdnbhvyqunck5hf97pckktzndx9cicwi2foaguoiypnq5lav32jout2albeepzu0jmo195hwxzyfqyuzmuxd59dww79zaszr4x93v4mi70xt5m7ojmgftwfcr6pvkjnsps9b6iqia51laxf5gxftm40zp4w3fe3hgrav0vzusjuvchys2pqs4p83edmbounl0jme7l8gpz33r3i1qz871d2qxkjjtg8e5mk0wlzm2t7shje9fxy2gxc2gz2gbwzp0rqypjhi12txt99yznnnejot3065t6pjrpl2dd874qenmgi3r3z7ilv03xkmy5b5foh5myqxnrw19ahtczx1sdhjo1sprr3th0ttolkhlxgj1xpgqwmbfecc7u1dq02b7k98dorf7t3d4e61a6ywkigfdrxdg0qri9o27ay9ethcgkj975isrqgcohmfm1fi54lshdvptgspr89bknusbpxk5v5huc5dgka8xq287nni317fd1oomeoa94ee3rt6inj8w8x269espmrlydlbta2vun1txzzows23sxmqbqtbejww18td0oen9387pr6mh8bcx6nx9wimughqgddw0cpih02u9i0hbnr60pjypvo7a23qp80slb881rnw7cgvf1xn3z29803cz9mw9v6crydm64ajz4dt7z0pe9fdgafk1jap72ofsakpp4kduj9po03j2bs3ei3hxn5fy0aduu97yx1ko21unrgl94g8gdlfgu7nrvjpgge8z5qryusfsxblzr6mmkqswdq13uzmq1jaxgkntvahb0yiiidsaj678s4pkvv88zvt9vn30eenoh6vogjwmnsbetjbj24u21qcfohu2lmn3et13eor0i7gwkzpdahy096fzfkx9uz8ob35ca048fb59cxu0e96ik1cqui4umgjd8hia19a8yykv776lj9m5051cufk2nqdont6pyjnj4gpfmw0f38kt5lyutofa307r4qzlv2somi55ur60zrnmg859t6o2beosim59rvuobdce7gxcn76mwxmik5j3v9l81bbtvr17q9gznhejfaw65vlpdi1lk1hojivrh9fglrws814lln0seef1nypzukhfey0134i1j42f3hhrb4x51keg864jc0fje9p9qmofb02lfz9sgad5132w273e1593rvc4oi1jlcyc8gheon57tu58cq1fkuzitbqxtg7ulif24b2ijija37rfrm54o28nzfuiwt7ybwtcypseqhxqv6z4d0ezqjbh3z6nct0vz5gs58o9lcj4owz1qaf4wgz71scj9o41er98i9r2kp3ijv4a3kf5apznenrvsqh3iq3ak3vdtr6ud6oo8d40jdxax2hu0jl6de0o8kpa6mziomwdjkcrf72wh84k07f10x8q14lkr87wy4v7b7zcj5tnnxp3tcr0xd1bhbgxyr73vm4nrqjeok0r8griynsu7to0wjv3yzixwsib1zypumucr3opcsxu60r05q3fnaez1otolhajbyocsh14xqeygaytjzyx0ilpejffyyfbs507ct3qwqksi6w7pcbcisk5chnir1tlah6b64jc1rxhpl8okt7u79h2vo1qn9zu5st07jsp372suzsay5plfp0bdu2ha6pw4ax406sust5s3vvakt4iy3du9nqgrykjlzizmozj2qy6s8rsu9yeajamy7cf7lhotdcwg5sznyt3zq5azlwza68s0qbuf71rckh9a6rhxukketh2lclrj0zpthpohq7uvlave39e3dvxs5dxficac4yta949c9p3dokmem8nnb29esxqojp6ngv1kl4pfh1fyx8qqdlyymsghjy8rc9rzgqyth590p3difgyvreux8odasehhgu29aaabfrv52e260whaanu9vq2q6bdi8iiffaazlq8spc1y3k0iylnfiq5xgjpuwn9pivq08apeap8t7kfdv0592kno2s3it4ip60844m8i3ylclkzqrzj15rel87r6vtzvcajfdvgha8vr32ckut12kwa8b1tgv32wm5k3h2km1vrduwt7ccz0q9y16dn4v1djljtmr6afv2gea2zyanipt5cex17fslw29f2nq57w3fjiwh2e2xy0oona7ef5gew7tf4dmzs1vqtzbrz51wocb1sgzg9bon743kfp3z4c97lwjbsboi1sy95h1o46d9ui6zxge6ft1unn6qh0c48tpxmnsvbltmxd5qbavwedjlbvnr6rqd2ae3n5g58kzgj9agdt5d9igpj5boi4rkj7s4gevyd7bmsfb6h7i0ecsoctmlkoipjlujp7o5xpznrmmt1nrhxu50emsv88xunzczd2pz06arigac44sw26hbhlwb11buhckis20scqmpbr730d51748oxqpsohcn0ab1cslz73lxch576iwwcrpytmiq6ng5nuljpifp64xaovnd3xy8o8g980gdsubx4h9yhrcnmdp8frl3y1qdxhfcb8rv4bjshilbf7lj7p71fyofagzi7giif7bm4wm5vtrv7ckohqrnu7me1z3uu6e88e2ecawqe77y9llzls5f8qns777gbxyhixv4q08ctunxwl2zse29skqbxzgrimwgeb8lpkp326ry7u9f1ksyk2y95xg3hzhjr9kz47d111kon3iqj6ogaswvn3od875vtab7dycuqka1dtfvulu2k3dy0xxrg3ucjirdqw1c3n50j5g6wpwo8bujp10dyl7dohmjfrc0jfbddot14tze5g6nx5041bkplxy4nwsttsf2qf6pa7bon5vjtiyehag30i7342n0zlgfgbm29qhqgsmedtu9v9khlejvg2l25zvpe0uslkvv7rwkp6fex48k0p9yn9ia4zlyaw1ja9bpnvuxiwcclgrhabg2zpfmtmdkw7cbb4kljenveduw30k14dyru8f8akw7d4v92yajtdapry8vkci30qznp3oci34su6x6i73npsjc1kaqydh4g8ewka8c6wqxjj2y00t1rvrabhpn4opqlcm77d8h4mc1vkmb3s5otg5kgbwqkqtt4g8wjbag2vpdu026c2842fnon3s1w0j6g3s5439rcn1p1s9ddd9h2wg2kpb9v71w8vq4h1kdm446o1dytvx5yhn8uuf8tcp5gt84m98vzflhxc98ittp26ke8xf5488fp1qreuyk3u11ipwwwtbkzxb8nvcrz1aikzb8f1qe5yxuhj59x9tywdwebjbsuzs56feoourruf03qhoeoescpqyi0a023b1j62yfym8zljhnht376t0m8l28bs734avro73r9nicxuihb931ahd7ogbd9op4od24ez9qsn75rajmy3dpkwqivfysf1sgmwbkh8gafpdr9nsr8n61cd43f6jj8iqy1twc0pqu1h98b8d4jq7z0oq1kw7rsv453nu1yno2h4tei6r5lx8xk2ytldj1sapljbg9ztmx7g2jicwjoi2ue7kkepfl4za9ztdzxy4rvm7anhg076ul5hz5k942"
    # sub = "ki1rj2tj6jkyfhfcemnqaxe92pmmd6n1p411hxpzphmsbubjnm7mg1rgmjjbwan0gnbcy8n26mnxxncyuw6wghbxb9kwdm77ylg9x7cxnhxaj6kg1uuh75s7ucvmz60hahbgh4852x7g5tnbzzyy1xgbwjv1t77wgrwbbny3inm7xgvs1obctbpca2vd7xth5xggs2i77n3cbugn5fo1nnj2tt2nvsn5j9enu8gvv9upgtwjx2nf91j0rn7tngjnnan4b94n396a43zcqhix7771r82gfvym1mhw6puxjgjjx9f22c1r9z6jx7pxpjcuesxz91krw2b2jmpvlbsxjdsvzif0nxc246uh2mo1sy2pmjhxypzd1e6amhuydhgc5qbcxxu3tw4aagjj7cjpyvasrybr7468vh7eor9buuhax2noys5t3qgaswgiun2rpno6vye15p7mpvwus1q7eu934v1g7phnp0ukvbwsxrhrjjledvh5krx06nn6aegrzeo8escmghc203j41jaocnmex6cpdy9buwjqgw662ny65xfe2hvh8h7uw66sn7nk6pf3qppx1bycn7v7ismxb05tv6vhv1pyjaxtngzg1hnogjphdnl51b2trkbxgwn2faqpansjfso1ecr66fezj7jonxbbayuigjhee87e26gnw72hjgn76drmilnxnach8522og462166716jsqxqs1baj7cpxrs5sb5uwfr736193yz9niy78snu5kk6yhnsazqy6nw26be1nhem1uycw63gww6xsaoox4jmjx0gzmvp1funjyb7qg2x675au6slsnwv7xrgmg13hr8javjiw474uykn67yb7r8wmyqieinubpjgmp0unybdgj0c0mhefa3ich77yhg75apqmgnghghqtnbmsv9mhp12bngujpnw5gx1rmyjs1pnb8kvj1xby0nnp55m2ujncxmu7yihxu6augagy179tavayw8jjm2yriu9u7dy4b1brh6n3vvjs0b4mybob2jyxgvbuby8l3ihdopnwghrjy1jyfe6y3xb3mtj1jzchhu768gyjjcg7mrmxu7h12xaznefx68phamgmbgsm0nky3jevw656j8b7hhjnvb8bsksw2nmgt67kmnswbs32q1invguau29dsb7thhzgn6ro61h3jphtm3es56n2nn1ryc3lm1ncfbv53h66hyz2mbvu1a67dnbhvy6uacbgjxp3pykbtzadx9c2yvixxna1hninpaq5lnv32rnhj2agbeey7hhr7o695hvxznfqnu77hxw5pwvv7p7ah7e4bp3v47230bj573oj7gxtwfceuyvkrasphpbui62n56gnxxg1xxjm40zp4v3febh1ravhvzusrhvyhyhxpqhmy8bcdmsnualhr7c7l81p733rbi6q7536d2qbbrjtg8e57bhvg7m2j3sjrc9fbyxgbc21z2gsw7y0rqyprhi12jxj9pnzannejnjbh65t6yjepg2ww5346ea7123eb77igm0bxkmygb5xohg7n6bnew1pahjczx1hdjjo6hyrr3th0tjnlbhlb1j1xpg6vmbfccy7u6dqhxb3k95dnrf7jbwmc66n6yvkigxwrbd1h6ei9n27nnpejhygbrp7gihrq1coj7fm1f25mlhhdmyjghye59skauhsyxb5mgjhc5dgbn5b6x83nni313fd6onmcon9mcebeju2nj5w8bx6pchpmegnwgstnxvhn1jx77nvh2bsbmqbqtbcrvw65jw0oeap387peumh8bcxuab9v27u1hqgdwwhyy2j02up20jsneu0yrnpvo3ax36y5hslb581rav3ygvf6xabzxp8h3yz97v9muyeydm64nj7mwj370ye9fw1axk1jny32nxsabpymkdhrppo0bj2bsbe2bjbn5fyhnduhp3nb6kox6unr1gp4151dlf1h7nrmrp11c8z56ryuhfhbbg7eum7b6svwq13h7766rab1bnjmnjshn2iidsnru35s4ybmv557mj9ma3hceanh6vogrv7assetjbr24u216yxnhh2lmabet63cnr0231vbzydnjy096xzxkbphz8nsbgya048fbgpcxhhc96ib6c6uimhm1jw5j2n69a5ynkv736gr97g051yuxbxaqdontupyrar41pfmw0f38kj5gnujnxab03rm67gm2snm2g5ueuh7rn7g55pj6o2scosi7g9rmuobdye3gbya7u7vbm2kgr3mpg81bbtme67qpgzahejfnwu5mlywi1gb6horimej9xggewh51mlla0sccf1nnp7hbhxcnh134i1rm2x3hjebmb51kcg5umjyhfrc9ppqmofb02lfz9s1adg1bxw27bc6g9bemy4oi6rlyyy8gjeoag7jhg5cq6fbu7its6xtg7hl2xxmbx2r2jab7rfem54o28azfh2wj3nbvjcnyhc6hb6mu7mwhczqrbjb7uaythm75gh55n9gcr4ovz16nx4wgz31syr9nm6er952prxkpbirm4nbkxgnpznenevs6hb2qbak3vdje6uwuoo8dmhrdbax2juhjl6dchn5kpa6772nmvwjbyrf72wh5mb07x60x5q64lbe87vn4m7s3zyj5jnabpbjyr0bw6bhs1xne3bvm4ne6renb0r5gr2nnsh7to0wjmbyzibvsis17npumucrbnpysbh60e0g6bfanez6ojnlharsnoysh14b6cngnnjr7ybh2gycjxxynfbhgh7ctbqwqks26w3ycsc2hkgcha2e1jgnjus6mrc1ebhyg5okj3u39j2vo16ap7u5hjh3rsyb3xhhzsny5ygxyhbwuxjn6pv4nxm0usuhtgh3vmnkj4in3dhpnq1enkrlz27mnzjxqn6s5esupycajnmn3cf7ghntwcv15h7nnt3zqgazgv7nu5sh6shf76rcbj9a6ejbhkbcjjxgcgrrh7pjhpnhq7uvlnmc3pebdmxhgdbx2yacmntnpm9ypybdob7cm5anbxpehbqorpungv1kgmyxh6xnx8qqdgnymhghjn5ecprz16ythg90p3w2fgnmreub5odnhejh1uxpnnabxemgxe26hvhanahpvqx66sdi5iixxaa7g65hyc1ybkh2ngax2qgxgryuvn9p2m608npcnp5j3bxdmhgp2bnn2sbij42y6054mm823ngygk76e7r65reg87e6mtzvynrxwm1jn8mrb2cbhj12bwa5s6tgmbxv7gb3h2km6mrdhwt3yyz0q9y6udnmm1drgrtmeunfvxgcn27yaaipt5ycb63fsgwx9xxnq57wbxr2vj2exxy0nnna7cx5gcw7jfmwmzs6m6j7sr751vnyb1h171pboa34bbxpbzmy97gwjbhboi6hn9gh6nm6wpuiu7bgc6ft6unn6qj0ym8tpbmnhvsgtmbd5qbamwcdjgbmnr6eqdxacbagg58b7gr9ngdjgdp2gyrgsnimrbr3s4gevnw3bmsxsuh320echnytmgbo2prgujp7ogxy7aemmt6arhxughc7hv58xunzyzwxp7h6nrigny4msv26hbjgwb61bhhyk2sxhsy6mpse33hw56348oxqyhnhya0nb1yslz7bgbyhg362vwcepyj7iqun1gnuljyixpumxnnmaw3xn5o5gp50gdhusx4hpnhrca7wy8fel3y1qdbhxcb8ev4srsh2lbf3lj3y76xnoxagzi31i2x7b7mvmgvtrm3cbnjqrnh77c67buu6e55exeyawqc73yplgzlhgx5qns333gsxnj2xv4q08ytunbwlx7scxpskqbx7grimw1cb8lpky3xury7h9f1bsnk2n95b1bj7hre9kz43w666knn3i6r6ognswvabod87gvjas7dyyhqkn6wtfvuluxb3wy0bxe1bhcr2ed6w1cba5hr51uvpwo8bhrp10wyg3wohmrfrchjxbwwnt64j7egguab5046sbplbn4nwsttsxx6f6pn3snngvjtiychagbh27bm2ah7ggx1s7x9qjqghmewjh9mpbhlcrvgxl2g7myc0hslbmm3evbp6xcx45khypynp2nmzgnnv1jn9bpavhb2wyylgejab1xzpxmtmdbv3cbb4kgjcaveduvbhb1mdyeu8f8akw7wmm9xnajtwayey8mbyi3hq7ap3ocib4sh6b6233ayhjc1baqnwjm18cwbn5yuv6bjr2yhhj6evrnshyamnp6lym33w5h47y1vb7b3sgoj1gb1sv6k6jt4g8vjbag2vywuh2uyx842fnoa3h6v0r6gbh543pecn6y6hpdwdpj2wg2kyb9m31w5m64j6kwm4m6n1dyjmx5yja8uhx8jyyg1j8mm95vzfljxyp5itjyxube8bxgm88xp66echnkbu612yvw"
    # mappings = [["v", "r"], ["n", "b"], ["y", "g"], ["m", "3"], ["z", "q"], ["t", "u"], ["3", "l"], ["4", "7"], ["t", "6"],
    #  ["9", "x"], ["f", "s"], ["5", "m"], ["l", "5"], ["3", "t"], ["8", "b"], ["7", "p"], ["p", "q"], ["l", "t"],
    #  ["2", "b"], ["g", "b"], ["m", "u"], ["r", "o"], ["4", "c"], ["r", "s"], ["i", "d"], ["m", "o"], ["p", "d"],
    #  ["a", "f"], ["r", "i"], ["o", "r"], ["q", "8"], ["3", "v"], ["f", "i"], ["m", "a"], ["r", "k"], ["n", "8"],
    #  ["5", "q"], ["5", "k"], ["7", "s"], ["h", "v"], ["2", "8"], ["x", "q"], ["f", "w"], ["6", "j"], ["4", "n"],
    #  ["k", "i"], ["v", "a"], ["c", "b"], ["5", "v"], ["f", "4"], ["c", "v"], ["w", "c"], ["s", "t"], ["6", "0"],
    #  ["a", "i"], ["n", "h"], ["g", "d"], ["y", "0"], ["g", "6"], ["r", "g"], ["0", "e"], ["o", "t"], ["c", "s"],
    #  ["2", "y"], ["4", "b"], ["y", "6"], ["b", "g"], ["s", "j"], ["l", "r"], ["p", "k"], ["x", "1"], ["6", "s"],
    #  ["l", "7"], ["a", "g"], ["8", "k"], ["h", "l"], ["0", "o"], ["s", "9"], ["h", "k"], ["a", "7"], ["1", "6"],
    #  ["v", "u"], ["5", "g"], ["2", "3"], ["g", "j"], ["0", "7"], ["i", "o"], ["b", "z"], ["s", "3"], ["o", "m"],
    #  ["9", "j"], ["9", "0"], ["8", "h"], ["u", "e"], ["4", "d"], ["h", "p"], ["8", "j"], ["x", "5"], ["t", "h"],
    #  ["a", "k"], ["d", "j"], ["m", "2"], ["a", "v"], ["8", "z"], ["3", "c"], ["5", "4"], ["d", "a"], ["j", "n"],
    #  ["4", "v"], ["5", "o"], ["6", "u"], ["n", "7"], ["p", "n"], ["f", "a"], ["p", "z"], ["w", "9"], ["x", "s"],
    #  ["1", "r"], ["7", "3"], ["y", "t"], ["6", "7"], ["u", "c"], ["7", "x"], ["1", "s"], ["2", "j"], ["e", "3"],
    #  ["i", "s"], ["5", "i"], ["1", "m"], ["8", "4"], ["t", "a"], ["b", "y"], ["0", "f"], ["o", "6"], ["8", "s"],
    #  ["2", "6"], ["0", "p"], ["3", "8"], ["m", "0"], ["i", "f"], ["a", "6"], ["u", "7"], ["j", "g"], ["h", "a"],
    #  ["y", "4"], ["m", "j"], ["3", "w"], ["d", "l"], ["h", "b"], ["l", "9"], ["u", "z"], ["b", "6"], ["h", "5"],
    #  ["x", "t"], ["t", "m"], ["f", "q"], ["4", "t"], ["i", "m"], ["c", "d"], ["d", "p"], ["q", "w"], ["0", "g"],
    #  ["b", "9"], ["g", "i"], ["6", "8"], ["k", "9"], ["b", "l"], ["d", "r"], ["u", "i"], ["q", "k"], ["b", "0"],
    #  ["t", "2"], ["g", "r"], ["1", "n"], ["6", "g"], ["3", "z"], ["p", "4"], ["m", "6"], ["g", "7"], ["1", "y"],
    #  ["s", "p"], ["5", "9"], ["e", "1"], ["r", "0"], ["b", "e"], ["m", "d"], ["4", "x"], ["7", "g"], ["s", "7"],
    #  ["0", "a"], ["7", "c"], ["9", "s"], ["s", "e"], ["j", "i"], ["q", "3"], ["6", "w"], ["b", "1"], ["q", "f"],
    #  ["4", "i"], ["p", "o"], ["f", "8"], ["x", "r"], ["7", "n"], ["j", "m"], ["8", "6"], ["c", "m"], ["8", "t"],
    #  ["7", "1"], ["6", "3"], ["p", "6"], ["f", "3"], ["j", "z"], ["e", "o"], ["h", "6"], ["h", "g"], ["u", "v"],
    #  ["d", "q"], ["j", "x"], ["4", "q"], ["i", "e"], ["c", "x"], ["1", "h"], ["p", "w"], ["f", "m"], ["c", "n"],
    #  ["2", "z"], ["n", "f"], ["k", "f"], ["8", "e"], ["m", "t"], ["y", "u"], ["j", "s"], ["b", "5"], ["z", "8"],
    #  ["j", "a"], ["v", "z"], ["n", "v"], ["2", "n"], ["6", "v"], ["0", "r"], ["s", "o"], ["l", "j"], ["l", "d"],
    #  ["9", "m"], ["7", "k"], ["5", "h"], ["0", "c"], ["w", "y"], ["r", "4"], ["f", "p"], ["0", "m"], ["b", "t"],
    #  ["0", "w"], ["5", "p"], ["l", "8"], ["d", "1"], ["d", "y"], ["p", "f"], ["s", "6"], ["n", "z"], ["y", "7"],
    #  ["b", "i"], ["8", "f"], ["g", "c"], ["q", "v"], ["e", "w"], ["f", "g"], ["z", "p"], ["d", "b"], ["6", "h"],
    #  ["r", "b"], ["z", "9"], ["w", "z"], ["8", "y"], ["e", "p"], ["t", "q"], ["e", "t"], ["5", "s"], ["v", "c"],
    #  ["8", "r"], ["j", "5"], ["n", "d"], ["i", "g"], ["g", "u"], ["2", "e"], ["z", "s"], ["p", "m"], ["1", "w"],
    #  ["d", "4"], ["i", "0"], ["w", "v"], ["k", "a"], ["3", "g"], ["4", "5"], ["5", "y"], ["4", "f"], ["m", "r"],
    #  ["t", "9"], ["5", "a"], ["w", "0"], ["d", "i"], ["9", "n"], ["2", "o"], ["l", "u"], ["f", "0"], ["4", "a"],
    #  ["z", "c"], ["n", "t"], ["g", "3"], ["m", "q"], ["a", "j"], ["x", "h"], ["1", "f"], ["d", "o"], ["j", "9"],
    #  ["v", "t"], ["t", "c"], ["i", "a"], ["h", "w"], ["v", "l"], ["r", "f"], ["p", "t"], ["1", "5"], ["p", "a"],
    #  ["m", "1"], ["u", "x"], ["8", "5"], ["5", "r"], ["3", "u"], ["f", "k"], ["g", "1"], ["z", "a"], ["f", "u"],
    #  ["g", "4"], ["l", "x"], ["e", "f"], ["f", "j"], ["i", "q"], ["3", "a"], ["0", "l"], ["z", "y"], ["o", "x"],
    #  ["g", "w"], ["a", "2"], ["j", "8"], ["d", "h"], ["h", "j"], ["v", "g"], ["9", "b"], ["t", "v"], ["u", "3"],
    #  ["9", "c"], ["j", "r"], ["c", "z"], ["b", "s"], ["w", "r"], ["x", "8"], ["2", "w"], ["h", "y"], ["b", "d"],
    #  ["0", "t"], ["s", "c"], ["o", "w"], ["z", "5"], ["b", "4"], ["e", "2"], ["f", "1"], ["r", "d"], ["4", "2"],
    #  ["o", "9"], ["9", "5"], ["9", "w"], ["f", "2"], ["1", "p"], ["n", "c"], ["s", "1"], ["5", "b"], ["e", "8"],
    #  ["5", "3"], ["z", "3"], ["k", "b"], ["2", "p"], ["5", "d"], ["l", "2"], ["c", "8"], ["k", "m"], ["r", "u"],
    #  ["g", "9"], ["y", "h"], ["f", "l"], ["2", "q"], ["v", "k"], ["l", "i"], ["s", "h"], ["m", "w"], ["z", "k"],
    #  ["m", "h"], ["k", "1"], ["0", "s"], ["p", "3"], ["o", "l"], ["9", "2"], ["z", "7"], ["0", "j"], ["d", "g"],
    #  ["a", "s"], ["j", "4"], ["4", "l"], ["c", "k"], ["5", "c"], ["6", "l"], ["o", "n"], ["w", "l"], ["x", "v"],
    #  ["l", "3"], ["d", "9"], ["l", "4"], ["z", "m"], ["u", "w"], ["r", "8"], ["i", "p"], ["y", "r"], ["3", "k"],
    #  ["j", "3"], ["p", "l"], ["2", "s"], ["g", "2"], ["v", "o"], ["q", "l"], ["b", "p"], ["k", "h"], ["y", "m"],
    #  ["v", "8"], ["h", "f"], ["m", "s"], ["3", "s"], ["5", "f"], ["l", "f"], ["h", "o"], ["i", "h"], ["g", "k"],
    #  ["z", "e"], ["1", "k"], ["y", "f"], ["o", "k"], ["7", "i"], ["o", "c"], ["e", "i"], ["j", "7"], ["q", "4"],
    #  ["o", "4"], ["o", "h"], ["h", "i"], ["j", "c"], ["n", "r"], ["y", "3"], ["d", "c"], ["y", "9"], ["o", "b"],
    #  ["a", "r"], ["q", "6"], ["n", "m"], ["c", "o"], ["e", "d"], ["6", "z"], ["j", "o"], ["o", "j"], ["s", "q"],
    #  ["f", "e"], ["2", "t"], ["h", "3"], ["9", "i"], ["7", "b"], ["h", "x"], ["8", "g"], ["1", "a"], ["p", "g"],
    #  ["d", "v"], ["8", "w"], ["u", "k"], ["w", "7"], ["d", "n"], ["c", "a"], ["l", "6"], ["8", "7"], ["4", "y"],
    #  ["9", "z"], ["9", "k"], ["h", "e"], ["0", "y"], ["a", "h"], ["1", "t"], ["x", "p"], ["l", "p"], ["3", "r"],
    #  ["f", "n"], ["d", "x"], ["p", "s"], ["4", "s"], ["p", "i"], ["0", "2"], ["3", "5"], ["y", "b"], ["m", "8"],
    #  ["q", "s"], ["s", "8"], ["8", "d"], ["s", "k"], ["q", "u"], ["v", "b"], ["k", "s"], ["1", "9"], ["k", "7"],
    #  ["z", "0"], ["v", "j"], ["n", "3"], ["9", "o"], ["h", "7"], ["7", "9"], ["y", "5"], ["0", "k"], ["c", "p"],
    #  ["0", "3"], ["5", "1"], ["d", "f"], ["q", "g"], ["o", "g"], ["i", "5"], ["m", "c"], ["q", "m"], ["b", "u"],
    #  ["q", "a"], ["v", "0"], ["z", "h"], ["6", "f"], ["v", "n"], ["c", "1"], ["w", "s"], ["q", "1"], ["p", "y"],
    #  ["k", "4"], ["1", "x"], ["d", "u"], ["u", "n"], ["1", "v"], ["l", "o"], ["x", "7"], ["f", "9"], ["e", "k"],
    #  ["7", "v"], ["x", "l"], ["u", "p"], ["u", "f"], ["t", "j"], ["4", "e"], ["4", "h"], ["b", "8"], ["a", "p"],
    #  ["3", "4"], ["c", "0"], ["w", "h"], ["k", "0"], ["i", "z"], ["z", "r"], ["9", "l"], ["9", "6"], ["v", "5"],
    #  ["t", "b"], ["u", "8"], ["f", "v"], ["8", "x"], ["1", "i"], ["z", "j"], ["8", "i"], ["b", "a"], ["f", "5"],
    #  ["a", "3"], ["p", "r"], ["e", "q"], ["x", "d"], ["e", "6"], ["n", "s"], ["w", "u"], ["i", "9"], ["e", "v"],
    #  ["9", "t"], ["u", "0"], ["v", "4"], ["v", "h"], ["x", "y"], ["7", "w"], ["3", "p"], ["5", "w"], ["p", "5"],
    #  ["6", "p"], ["a", "z"], ["v", "m"], ["c", "7"], ["3", "y"], ["i", "k"], ["0", "q"], ["6", "e"], ["9", "y"],
    #  ["7", "r"], ["d", "5"], ["2", "4"], ["f", "t"], ["t", "n"], ["6", "c"], ["c", "5"], ["k", "l"], ["1", "3"],
    #  ["2", "0"], ["i", "u"], ["g", "x"], ["c", "i"], ["j", "q"], ["l", "1"], ["i", "4"], ["t", "r"], ["g", "h"],
    #  ["h", "4"], ["n", "4"], ["l", "0"], ["a", "4"], ["6", "2"], ["2", "m"], ["s", "d"], ["0", "x"], ["7", "d"],
    #  ["k", "d"], ["w", "q"], ["g", "z"], ["t", "s"], ["y", "8"], ["i", "c"], ["8", "u"], ["3", "9"], ["h", "2"],
    #  ["x", "j"], ["l", "z"], ["1", "7"], ["f", "6"], ["6", "t"], ["o", "a"], ["6", "y"], ["l", "h"], ["h", "d"],
    #  ["9", "8"], ["t", "p"], ["n", "i"], ["s", "x"], ["m", "l"], ["7", "6"], ["z", "2"], ["m", "x"], ["6", "4"],
    #  ["9", "u"], ["o", "3"], ["j", "f"], ["1", "2"], ["i", "t"], ["6", "5"], ["n", "x"], ["e", "9"], ["o", "u"],
    #  ["g", "y"], ["v", "d"], ["l", "n"], ["0", "6"], ["r", "t"], ["j", "u"], ["b", "r"], ["k", "r"], ["3", "d"],
    #  ["q", "e"], ["m", "k"], ["i", "7"], ["2", "u"], ["n", "9"], ["2", "d"], ["3", "1"], ["h", "c"], ["t", "4"],
    #  ["r", "3"], ["1", "j"], ["0", "h"], ["h", "z"], ["t", "d"], ["2", "l"], ["0", "1"], ["m", "e"], ["y", "j"],
    #  ["d", "0"], ["j", "p"], ["j", "b"], ["n", "6"], ["r", "v"], ["w", "6"], ["a", "u"], ["d", "3"], ["r", "l"],
    #  ["l", "k"], ["s", "a"], ["4", "m"], ["7", "h"], ["3", "f"], ["i", "l"], ["i", "r"], ["8", "o"], ["t", "o"],
    #  ["c", "r"], ["n", "5"], ["v", "i"], ["w", "b"], ["q", "j"], ["z", "6"], ["9", "a"], ["u", "2"], ["l", "s"],
    #  ["u", "a"], ["s", "0"], ["o", "q"], ["g", "a"], ["u", "s"], ["m", "g"], ["n", "p"], ["a", "t"], ["z", "v"],
    #  ["h", "r"], ["3", "b"], ["v", "p"], ["m", "b"], ["2", "x"], ["4", "1"], ["g", "s"], ["4", "3"], ["q", "0"],
    #  ["y", "e"], ["t", "f"], ["0", "z"], ["c", "j"], ["f", "x"], ["8", "9"], ["r", "p"], ["q", "7"], ["k", "v"],
    #  ["h", "9"], ["k", "e"], ["8", "v"], ["j", "v"], ["u", "9"], ["k", "5"], ["4", "0"], ["u", "1"], ["q", "r"],
    #  ["3", "h"], ["x", "g"], ["6", "a"], ["l", "m"], ["4", "g"], ["7", "5"], ["5", "2"], ["u", "4"], ["o", "7"],
    #  ["k", "u"], ["v", "s"], ["7", "8"], ["i", "8"], ["s", "l"], ["a", "m"], ["p", "v"], ["5", "j"], ["d", "2"],
    #  ["d", "z"], ["v", "y"], ["t", "0"], ["0", "b"], ["b", "c"], ["6", "o"], ["j", "k"], ["1", "d"], ["5", "0"],
    #  ["u", "o"], ["g", "q"], ["g", "0"], ["2", "h"], ["k", "x"], ["e", "a"], ["w", "p"], ["z", "g"], ["z", "l"],
    #  ["b", "v"], ["c", "l"], ["4", "k"], ["i", "v"], ["x", "3"], ["4", "8"], ["v", "x"], ["d", "w"], ["q", "z"],
    #  ["v", "9"], ["6", "9"], ["x", "b"], ["9", "v"], ["o", "p"], ["e", "j"], ["l", "y"], ["9", "d"], ["y", "d"],
    #  ["q", "9"], ["8", "1"], ["1", "z"], ["t", "w"], ["r", "y"], ["o", "d"], ["z", "4"], ["m", "y"], ["e", "s"],
    #  ["7", "j"], ["l", "w"], ["k", "3"], ["2", "c"], ["f", "c"], ["w", "g"], ["8", "p"], ["e", "b"], ["t", "g"],
    #  ["0", "n"], ["m", "i"], ["u", "l"], ["s", "i"], ["7", "q"], ["w", "n"], ["c", "h"], ["7", "a"], ["o", "v"],
    #  ["g", "8"], ["s", "5"], ["h", "t"], ["9", "3"], ["5", "6"], ["g", "m"], ["i", "n"], ["x", "e"], ["d", "8"],
    #  ["9", "7"], ["x", "a"], ["e", "z"], ["k", "t"], ["g", "n"], ["q", "n"], ["o", "0"], ["y", "l"], ["9", "h"],
    #  ["z", "x"], ["m", "5"], ["7", "y"], ["e", "0"], ["j", "l"], ["r", "5"], ["c", "9"], ["7", "4"], ["7", "0"],
    #  ["j", "w"], ["p", "x"], ["l", "q"], ["c", "u"], ["w", "1"], ["x", "c"], ["r", "x"], ["w", "o"], ["t", "1"],
    #  ["f", "r"], ["0", "4"], ["6", "r"], ["4", "p"], ["r", "7"], ["e", "h"], ["v", "e"], ["a", "w"], ["c", "q"],
    #  ["0", "5"], ["d", "s"], ["w", "3"], ["q", "x"], ["1", "0"], ["g", "o"], ["v", "1"], ["r", "6"], ["q", "t"],
    #  ["y", "o"], ["o", "y"], ["3", "2"], ["s", "u"], ["u", "t"], ["4", "9"], ["a", "b"], ["u", "m"], ["d", "7"],
    #  ["v", "q"], ["4", "r"], ["l", "a"], ["6", "n"], ["u", "d"], ["0", "d"], ["a", "5"], ["l", "v"], ["1", "8"],
    #  ["r", "2"], ["a", "l"], ["h", "s"], ["w", "f"], ["d", "6"], ["p", "j"], ["l", "g"], ["h", "1"], ["w", "5"],
    #  ["v", "3"], ["m", "4"], ["b", "q"], ["v", "7"], ["r", "n"], ["x", "6"], ["5", "8"], ["4", "u"], ["r", "c"],
    #  ["5", "e"], ["o", "2"], ["b", "3"], ["8", "q"], ["z", "w"], ["c", "2"], ["0", "9"], ["j", "2"], ["3", "6"],
    #  ["x", "f"], ["9", "1"], ["7", "e"], ["5", "z"], ["q", "i"], ["v", "6"], ["n", "a"], ["0", "i"], ["f", "d"],
    #  ["z", "t"], ["f", "y"], ["i", "x"], ["a", "y"], ["w", "j"], ["t", "7"], ["y", "1"], ["q", "p"], ["3", "o"],
    #  ["x", "2"], ["k", "w"], ["e", "y"], ["v", "w"], ["s", "b"], ["0", "v"], ["h", "0"], ["r", "e"], ["y", "p"],
    #  ["c", "e"], ["6", "k"], ["1", "c"], ["w", "x"], ["b", "x"], ["n", "y"], ["x", "n"], ["e", "r"], ["7", "z"],
    #  ["a", "o"], ["3", "n"], ["6", "1"], ["q", "5"], ["p", "9"], ["h", "u"], ["2", "i"], ["r", "j"], ["y", "q"],
    #  ["6", "m"], ["n", "o"], ["6", "q"], ["j", "h"], ["2", "k"], ["w", "d"], ["e", "g"], ["7", "m"], ["b", "k"],
    #  ["a", "n"], ["5", "l"], ["m", "v"], ["u", "6"], ["1", "g"], ["g", "l"], ["g", "5"], ["y", "c"], ["j", "t"],
    #  ["3", "7"]]
    solution = Solution()
    res = solution.matchReplacement(s, sub, mappings)
    print(res)
