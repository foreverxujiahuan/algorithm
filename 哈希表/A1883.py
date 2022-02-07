from typing import (
    List,
)

class Solution:
    """
    @param K: an integer
    @param keywords: a list of string
    @param reviews: a list of string
    @return: return the top k keywords list
    """
    def TopkKeywords(self, K: int, keywords: List[str], reviews: List[str]) -> List[str]:
        # write your code here
        keyword2cnt = dict()
        reviews = set(reviews)
        for keyword in keywords:
            for review in reviews:
                review = " ".join([c.lower() for c in review.split() if c.isalpha()])
                if keyword in set(review.split()):
                    if keyword in keyword2cnt.keys():
                        keyword2cnt[keyword] += 1
                    else:
                        keyword2cnt[keyword] = 1
        cnt2keywords = dict()
        for keyword, cnt in keyword2cnt.items():
            if cnt in cnt2keywords.keys():
                cnt2keywords[cnt].append(keyword)
            else:
                cnt2keywords[cnt] = [keyword]
        sorted_keywords = []
        cnt_list = sorted(list(cnt2keywords.keys()), reverse=True)
        for cnt in cnt_list:
            temp = sorted(cnt2keywords[cnt])
            sorted_keywords.extend(temp)
        return sorted_keywords[: K]


if __name__ == '__main__':
    k = 21
    keywords = ["mmebli","zooi","jolbc","akos","dhu","hcchht","dyemw","xzadxn","vel","duop","bkm","omlm","udhxve","nnhotj","qvp","tba","cmbyu","bdpig","msxgg","tbd","erkcq","nowrp","epide","nqc","ndqsq","gnaq","olqmrm","zuwt","qng","wqq"]
    reviews = ["SHEGGP zIFd Duop YPAwF ftS ovO cgQ olqmrm TcXLJ OEwNd sUw","Wqq Qmy PMEB Cmbyu otQZZ bdCz Bkm Olqmrm snwG cdeCQr","cyoKJT fQOEj sSm pCdeuA Cmbyu udhxve bkm zuwt dxhjTR Qng AxUI akos mwZFz SWiBxZ","YsINj bmOws MqUlHQ iUBI bwsF ipJOJ tpU udHrR ySk LcDOtu Jolbc Tba UPQ gnVuK oSJ FzYAIT","UJvrm SIWYcu cmbyu omlm UqVm duop Mmebli JWwFH GAVmrO IQfbe jAnCmB OMDY vlS bpInZ","Papi omlm COtQAK Tba BEbP Olqmrm kpbX mgo mmebli yHYRLo Wqyji nqlE ASn Zuwt PSHY qMAp","hwAoh hcchht nLAz RXbLXx qng eOJ","aFFKj Qvp udhxve NANo ZlGQ xzadxn Bdpig wqq ABVzqj GrudYj OQECXg Jolbc qFJI TexHTx","CcO Tbd ZYfnnr foYs Olqmrm bdpig dnkNr cbJHo agH Xzadxn MuCxgM Ndqsq xXFi Gnaq VUMUPw HABRRs Bdpig","Nowrp UVHA nnhotj CAk Olqmrm mmebli xqepfz TYxoO dyemw Gnaq","ySsT erkcq aNHGR vZfH DAuWSg DIF zdYtj olqmrm UIJDR gnaq Akos yPT Bkm","Wqq UxgJ Gnaq kKvaoe Gnaq AWoxbv msxgg xff cmbyu NfUdxJ Duop ijp mmebli tRA hmxK duop FoTv UCIjgK","bURZ MOKC SRvf Nowrp qqIhE HEUk BxS ahfHT","gkC gnaq Msxgg zmHXS bkm fVno lwgCPA MTqUCD csCLRS Bkm Epide CpRH RavjE zooi Xzadxn PbDpUO TUsJU","Xdz nowrp vIv Msxgg xzadxn IWelwi xQHnEW Wqq FizBl Kzx oDnZ reuNB omlm erkcq rnjdNV nqc cmbyu whr","SdDB lhyUvH nnhotj jPx ocDfZM Cmbyu pFaEI Zuwt","DAcL gejgW tHg zjY WJJx rjUCLN","xtR ldtW TJLoG Olqmrm aQZVE NJk Erkcq gyOc Jolbc ngQI mmebli Olqmrm","Hcchht ngE nlUsGQ MGvi RycLAT jeuDYJ","bhj erkcq Tba jBmzAg dhu bNsm Erkcq dhu tbd","TJOzBn Qvp GmMSMV xxpAY dVWBfx sjS Zooi","Tyog tbd ngum Emw WAywfT mkVCz eII","gbEEW iFwKe Nqc ndqsq wqq WWOU Xzadxn VvD IcD Erkcq","SsV ugb IbsvLv WnMI hyik qXA","jolbc xzz IPh AgmMO UYpu Zuwt Hcchht omlm DeoOX yLhakg xzadxn tJtDWT olqmrm dyemw HVJOsV","NeZJmr nnhotj GyekA UXzYAX Nowrp FWA BYv Udhxve Gnaq cmbyu iiwe flynxV vel KOf Cmbyu cmbyu PXsCNG gAa","ngdGqx hWoe LAjnRG oQjbU Lwh Cmbyu swKiUM XyHE WjMB nowrp KLhKYH riv Mmebli ANHx RpapZ","DnedbG UWuOcW gIOxdr nowrp KJm tba mmebli","tMfth YpsY cmbyu mdX sebZp ideIML olqmrm dhu Nyk Epide KoVQoL","Akos nowrp fLE bZCiJg epide SFn GwF Hcchht VLq XZuIn Erkcq deRm SgH qfbY ayEVCt gwzP","Hcchht Dyemw zqZtz tke DbZcb Omlm tQXhkC akos omlm qvp RToFE LZlmF Gnaq SgJEi flaNLc bkm UDDk UUu sWmKr","vynInD wqq aUDwM gnaq Dhu LtVm hyMTj Bdpig","VjGE Bkm FtzDIe qWueN qng auQ PHpdtc ATh VbaZhI eSZbX llVlzm Ykx jolbc cXBoY Akos","eNjZT zsYDgp QbPuF sCrfcU pNSImB wUqrf DIMt NkrD aFVw fwOJRx Olqmrm Vel Jolbc","erkcq mmebli wUXbN PZS lNw erkcq EHQXk Wqq yhYPCs TFmzH","GmvibP zoT tlZrK veqtE IRZu IPdx kfL EPmy EfkbL iLD Xzadxn AxLkZK aMgz XiE EdKNaQ eLsfIT yIcWGo","pdk bRpP Xzadxn hIUsyx XmVsWE BRwPO LPx Nnhotj Jolbc bdpig","Ndqsq GAJ kySL kaXAdT YaYleJ pQw zUJN rPLZbM OBubp farO xsqb ENcd","HLeboz nnhotj tbd Hcchht cStHr Ndqsq VdeTi wGh udhxve Lqtq cOp bEIu qodUz","vel gPBS Eqy aPkl bkm wiOS nWYg nnhotj hGpe uHOMYw YmO IFuiN PgR Erkcq","Bdpig qng beTPY PJxg Zooi","UhpVx UCCq jXWdJ sSARG Qvp WusnjS qKcRM ptvjQR","DWMEL WmuwfH mFNs Vbem Ndqsq QyiH iHsaE nvbMh dyemw iYZ wqq rOiYa VgJvkP Gnaq Gnaq","bkm Hcchht Mmebli EtcaHK LPxpHT Zooi yOlJ VDAMN aiVvoO Nnhotj nowrp fTGU Udhxve","tba uEcQgv GrZemh Srx zreMo Duop yucDsp Nrsa LIgZF mLkGXX HpTG mmebli sBmGY ydgNmE HsP","QcK Iudbe qng yKrDlx IFG Zser Bdpig jGl bCD pglave AoMH smS Duop bdpig ukpY","iJtsRf Epide BXFZh SsGg sZf CoZ nnhotj FjRaP UrHA","Dyemw hcchht dNMZkN EnknH jolbc Mtw ghAIMj sdLstq EPu Duop ZcyZW ThaGL KUahWq zMqvWz","MsS TxRb atxI wXJiuy yWdvXg hLs","rmlx wAilI qvp xsNuLo Zuwt OZm vsqBqV QIfa qCv jifElI QYyf olqmrm","AYcGp HdE cnOsnc Bkm Nowrp EeR SaJT QVpvWg zooi DDg Jolbc","VoM Jolbc fJkc SgIt NfZVI Hcchht JzR lmQsZY Erkcq qng fkSq jSd","iEqhSK cesL nnhotj rey qng elzX ArLj jympXV VjXqCy wjC","Dhu Duop ICpXe Flz ares lMav udhxve xykCo","Zuwt KmDp ANj AIK pXuu KrNXic","hcchht PYi HTko duop Vel xzadxn qng qvp dhu Dyemw AhiafX dyemw","erkcq hxoMKU VPo erkcq csadV YmlO Zooi OQRTDP Epide IWp","Udhxve epide xEXTqK udhxve fRris eSGY Vel YUfi XFB nqc yodt VcXb UcNA ZlFnkS Jbd fUBm AzW olqmrm Bkm","Hyjws zlXS msxgg izmU Elv wqq Gnaq qng","AOxSXc AzX zQFE erkcq xzadxn JPQr Nnhotj qqYSJ jolbc MbXaiQ omlm YSnMU EHKe cQsQot KUaj","nqc lIa dgmr QayhRF nowrp NTUef Wqq tWpQi udhxve rIh","Wqq ceBvv epide wqq Mmebli eHkVX Jolbc RzvYx tGXRTr erkcq dqYWJ pzUCRj MVcl","sys pORSKL ZMozzh Tba mrbH Nqc LOABI TTAL klhq","RhyEjN bOWNxB SbzHl eqMHP HTm yDFH kYEgwb msxgg FDFcuJ Zqy pVMjL Wqq UXxxLg ndqsq","Bdpig fBQIk vprkgw Nowrp vwfVF jolbc kyjpJ uKDAD nuipa vnneCC bkm PXoV xzadxn trpTJG bdpig epide bdpig","Qvp aWSoRW xgWY kTIy Msxgg Vel dnq cnMcO bdpig pyuiLC ycLX qya GHc Vel fTecu udhxve","mUYAv MlwTw JNlA FEVexJ hcchht","CkNIQ Akos okcgS bdpig HnuQ zooi qIwvnp Dsr tba cxvm","ndqsq LDhZ AiBixO tba vCEO KbV","ugfqrV IPo iBn SNUa UuVpkb nqc hFY WnfVw","xkJefz Mmebli Hcchht dmUIRQ riNE dhu uDQ mEI kHPU Ofu epide nowrp uUzow","vLG Ouc JDyb dyemw nnhotj Omlm qiLzM NXmzv wqq nFqZP wZTV uzdwgB bKsM","Qng iBhQX UIEX fpcO Omlm tbd PMPbwF mAgI bkm dhu jolbc ndqsq DWeufH Duop Qvp zuwt","lFI qvp dDr RrF TdWd Udhxve msxgg olqmrm Epide vLevX ABZc dhu zLDB bQJI qvp ucrT jlOi","Omlm Mtse ZoMzm akos duop","sjRzso bGJsg Epide sVU XIr iWkkv","Udhxve Ebeps TQYig Nqc mDpX Ehf Lqark bkm qOg gJxRUa ihOn","QnZLuq eIBhzD cccWv sOYi sxn KPqzbA Omlm MzH ZsLwpu wPNNL ZnmoY epide IcXpwH eNWb mmebli mUjHy","Dyemw vel fYlUvb Tbd LcXgQ bdGyPw nqc Tba sqKd Tbd OSWw oSaQJG dyemw fhMeba KsM TPjpd Erkcq nnhotj tba","zooi LRlysi mmebli gnaq bLRsEn Duop tbd wqq fmGUf eZRWGs QSljeh CjV Nnhotj MGQRoc aTOa hwh Ndqsq","OhB CBthF Omlm ojg setY XcRp byFC ryDyBv fAy GnEtq Blc alRKal Cmbyu Akos shw vOWLq rNKxn dhu vWxU","erkcq BXI vvs tcumT beSk qvp ghLKX lriZxX Ceduh Ivr qvp PgRwEh YczVY","Vel Zuwt egG Mxu Jpnt xTYT ApxsNy Nudk zuwt ZNKt xzadxn MjDeER oIeCO","qvp ZEqMhF qng soFVcu udhxve MNZ xBF Fyaf xzadxn Dyemw JFf gGkHjl sWj","tHWND gnaq IHlul Bkm CSx xkBNF nqc USpCSF nowrp Vel jolbc mek IipO tbd dyemw TFt Sfgr","Hcchht yvDJr epide LMkC LdM qng wCCiz SgXnl Udhxve Qvp Dyemw Sof dDZ","Razh vCx iQRhm msxgg bdpig lXd Akos Nqc MCeqwX jURMww GPfH","qng ofwLqj tLQGQb KbrE Erkcq ndqsq PpZKEQ tXwR nowrp Zooi YgCjO omlm nwV nJVsB akos Uhst","MEDm JHKu Omlm pQk Dyemw Hcchht Qng Ndqsq OewR cmbyu qng VcJ wju bkm jGz YuZ","tbd enXhQ RmEB GqCYM Bdpig CcKn FHlY yDYPl UTl BinGfV iyrRH tbNn RDEfSg olqmrm","pXVp lZw bdpig msxgg olqmrm gIvSGv KZo GuIGyM qvp Jxel USAs AGsG Hcchht Svi pSUnJm GaXOTY","fAq OaPI RxNHn cAM qSVUp erkcq KIK isWxD Tba zWQN qVUrk sOvy UyLmtU QLvFOv Cxh tbd cmbyu lJMw","iChT rKkO ynEcwR xzadxn WjH zuwt MGkQYT WzDryo","EcP xLuACn Dhu cmLys rcwGe JeK","JqMd ndqsq Wqq qqk KvjauD RUSSy Hcchht Wqq Olqmrm QJT QwLSrZ Udhxve LTuWb gzH","tVvP tbd lHP NYO akos SvWXfH HGGqk GayO aKRhSR dhu","CkI Vel cuutj nnhotj FsCO Qng","LRn liUue Cmbyu wgEAG olqmrm Nnhotj wOHjov JEQ rVXx nowrp","Msxgg NrcSTh hwM uQqy aJTUMi IIaq Akos","qng gpIptx knmG fSYQU dhu cmbyu cTed rSjPu Ndqsq Akos nyvHpi yOe pBgLx Akos Cmbyu xKMTUK sRN Hcchht hChrdu RDh"]
    solution = Solution()
    res = solution.TopkKeywords(k, keywords, reviews)
    print(res)

