# This code is copied from this page: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD2015
from datetime import datetime
start = datetime.now()
print("start time:      "),start
import ROOT
import sys
from ROOT import TFile, TTree
from DataFormats.FWLite import Events, Handle
from math import *
from ROOT import gStyle
from array import *
#from numpy import array
import math
import array

lines = [line.rstrip('\n') for line in open('rinv_0p01.txt')]
#lines = [line.rstrip('\n') for line in open('rinv_0p8_nofilter.txt')]
events = Events(lines)


#gen jets handle and labels:
handle_genfatjet = Handle ("std::vector<reco::GenJet>")
labelgenfatjet = ("slimmedGenJetsAK8")
handle_genjet = Handle ("std::vector<reco::GenJet>")
labelgenjet = ("slimmedGenJets")

#gen particle packed and pruned handle and label:
handlePacked  = Handle ("std::vector<pat::PackedGenParticle>")
labelPacked = ("packedGenParticles")
handlePruned  = Handle ("std::vector<reco::GenParticle>")
labelPruned = ("prunedGenParticles")

#gen MET handle and labels:
handle_genMET = Handle ("vector<reco::GenMET>")
label_genMET = ("genMetTrue")

#reco MET handles and labels:
handle_recoMET_noHF = Handle ("vector<pat::MET>")
label_recoMET_noHF = ("slimmedMETsNoHF")
handle_recoMET = Handle ("vector<pat::MET>")
label_recoMET = ("slimmedMETs")

#reco jets handle and labels:
handle_recofatjet = Handle ("vector<pat::Jet> ")
labelrecofatjet = ("slimmedJetsAK8")
handle_recojet = Handle ("vector<pat::Jet> ")
labelrecojet = ("slimmedJets")

DEBUG = 0

h_genht = ROOT.TH1F("h_genht","",100,0,3000)
h_genht_pfjet450 = ROOT.TH1F("h_genht_pfjet450","",100,0,3000)
h_genht_pfjet500 = ROOT.TH1F("h_genht_pfjet500","",100,0,3000)
h_genht_pfjet550 = ROOT.TH1F("h_genht_pfjet550","",100,0,3000)
h_genht_ak8pfjet450 = ROOT.TH1F("h_genht_ak8pfjet450","",100,0,3000)
h_genht_ak8pfjet500 = ROOT.TH1F("h_genht_ak8pfjet500","",100,0,3000)
h_genht_ak8pfjet550 = ROOT.TH1F("h_genht_ak8pfjet550","",100,0,3000)
h_genht_pfht800 = ROOT.TH1F("h_genht_pfht800","",100,0,3000)
h_genht_pfht900 = ROOT.TH1F("h_genht_pfht900","",100,0,3000)
h_genht_pfht1050 = ROOT.TH1F("h_genht_pfht1050","",100,0,3000)
# loop over events
count = 0
for event in events:
	pfjet = 0
	ncount = 0
	count += 1
	"""
	if count > 100:
	    continue
	"""
	#genjets
	event.getByLabel (labelgenfatjet, handle_genfatjet)
	event.getByLabel (labelgenjet, handle_genjet)
	fatgenjet = handle_genfatjet.product()
	genjet = handle_genjet.product()
	#genparticles
	event.getByLabel (labelPruned, handlePruned)
	pruned = handlePruned.product()
        event.getByLabel (labelPacked, handlePacked)
        packed = handlePacked.product()
	#recoMET
	event.getByLabel (label_recoMET_noHF, handle_recoMET_noHF)
	recomet_nohf = handle_recoMET_noHF.product()
        event.getByLabel (label_recoMET, handle_recoMET)
        recomet = handle_recoMET.product()
	#genMET
	event.getByLabel (label_genMET, handle_genMET)
	genmet = handle_genMET.product()
	#recojets
	event.getByLabel (labelrecofatjet, handle_recofatjet)
        event.getByLabel (labelrecojet, handle_recojet)
        fatrecojet = handle_recofatjet.product()
        recojet = handle_recojet.product()


        pfjet = 0.0
        for j in recojet:
                if abs(j.eta()) < 2.4 and j.pt() > 30 and j.pt() > pfjet:
                        pfjet = j.pt()

        ak8pfjet = 0.0
        for f in fatrecojet:
                if abs(f.eta()) < 2.4 and f.pt() > 200 and f.pt() > ak8pfjet:
                        ak8pfjet = f.pt()

	pfht = 0.0
	for g in recojet:
		if abs(g.eta()) < 2.4 and g.pt() > 30:
			pfht += g.pt()

	genht = 0.0
	pfjet450 = 0.0
	pfjet500 = 0.0
        pfjet550 = 0.0
	ak8pfjet450 = 0.0
        ak8pfjet500 = 0.0
        ak8pfjet550 = 0.0
	pfht800 = 0.0
	pfht900 = 0.0
	pfht1050 = 0.0
	for pa in packed:
        	genht += pa.pt()
		if pfjet > 400:
		        pfjet450 += pa.pt()
		if pfjet > 450:
		        pfjet500 += pa.pt()
		if pfjet > 500:
		        pfjet550 += pa.pt()
		if ak8pfjet > 400:
		        ak8pfjet450 += pa.pt()
		if ak8pfjet > 450:
		        ak8pfjet500 += pa.pt()
		if ak8pfjet > 500:
		        ak8pfjet550 += pa.pt()
		if pfht > 800:
			pfht800 +=pa.pt()
		if pfht > 900:
		        pfht900 +=pa.pt()
		if pfht > 1050:
		        pfht1050 +=pa.pt()
	if genht > 0:
		h_genht.Fill(genht)
	if pfjet450 > 0:
		h_genht_pfjet450.Fill(pfjet450)
	if pfjet500 > 0:
		h_genht_pfjet500.Fill(pfjet500)
	if pfjet550 > 0:
		h_genht_pfjet550.Fill(pfjet550)
        if ak8pfjet450 > 0:
                h_genht_ak8pfjet450.Fill(ak8pfjet450)
        if ak8pfjet500 > 0:
                h_genht_ak8pfjet500.Fill(ak8pfjet500)
        if ak8pfjet550 > 0:
                h_genht_ak8pfjet550.Fill(ak8pfjet550)
	if pfht800 > 0:
                h_genht_pfht800.Fill(pfht800)
        if pfht900 > 0:
                h_genht_pfht900.Fill(pfht900)
        if pfht1050 > 0:
                h_genht_pfht1050.Fill(pfht1050)


outFile = ROOT.TFile.Open("rinv_0p01.root" ,"RECREATE")
outFile.cd()
h_genht.Write()
h_genht_pfjet450.Write()
h_genht_pfjet500.Write()
h_genht_pfjet550.Write()
h_genht_ak8pfjet450.Write()
h_genht_ak8pfjet500.Write()
h_genht_ak8pfjet550.Write()
h_genht_pfht800.Write()
h_genht_pfht900.Write()
h_genht_pfht1050.Write()
outFile.Close()
print "# of events", count
end = datetime.now()
print("start time:      "),end
