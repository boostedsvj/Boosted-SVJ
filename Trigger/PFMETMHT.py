#This code is intended to computed the PFMETMHT120. The criteria is taken for the trigger selection on the year 2017 

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

lines = [line.rstrip('\n') for line in open('rinv_0p3_nofilter.txt')]
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

h_MHT = ROOT.TH1F("h_MHT","",100,0,1500)
h_genmet = ROOT.TH1F("h_genmet","",100,0,1500)
h_genmet_mhtmet120_pfjet450 = ROOT.TH1F("h_genmet_mhtmet120_pfjet450","",100,0,1500)
h_genmet_mhtmet120_pfjet500 = ROOT.TH1F("h_genmet_mhtmet120_pfjet500","",100,0,1500)
h_genmet_mhtmet120_pfjet550 = ROOT.TH1F("h_genmet_mhtmet120_pfjet550","",100,0,1500)
h_genmet_mhtmet120_pfht800 = ROOT.TH1F("h_genmet_mhtmet120_pfht800","",100,0,1500)
h_genmet_mhtmet120_pfht900 = ROOT.TH1F("h_genmet_mhtmet120_pfht900","",100,0,1500)
h_genmet_mhtmet120_pfht1050 = ROOT.TH1F("h_genmet_mhtmet120_pfht1050","",100,0,1500)
h_genmet_mhtmet120 = ROOT.TH1F("h_genmet_mhtmet120","",100,0,1500)

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

	px_mht = 0.0
	py_mht = 0.0
	ht_z_add = 0.0

	for j in recojet:
		if abs(j.eta()) < 2.4 and j.pt() > 30:
			ht_z_add += j.pt() 
			px_mht += j.pt()*cos(j.phi())
			py_mht += j.pt()*sin(j.phi())

	MHT = sqrt(px_mht**2+py_mht**2)
	if MHT > 0:
		h_MHT.Fill(MHT)

	px_met = 0.0
	py_met = 0.0
	for r in recomet_nohf:
		px_met += r.pt()*cos(r.phi())
                py_met += r.pt()*sin(r.phi())

	reco_MET = sqrt(px_met**2+py_met**2)

        pfjet = 0.0
        for j in recojet:
                if abs(j.eta()) < 2.4 and j.pt() > 200 and j.pt() > pfjet:
                        pfjet = j.pt()

	for m in genmet:
		h_genmet.Fill(m.pt())
                if reco_MET > 120 and MHT > 120 and pfjet>400:
                        h_genmet_mhtmet120_pfjet450.Fill(m.pt())
		if reco_MET > 120 and MHT > 120 and pfjet>450:
			h_genmet_mhtmet120_pfjet500.Fill(m.pt())
                if reco_MET > 120 and MHT > 120 and pfjet>500:
                        h_genmet_mhtmet120_pfjet550.Fill(m.pt())
		if reco_MET > 120 and MHT > 120 and ht_z_add > 800:
			h_genmet_mhtmet120_pfht800.Fill(m.pt())
                if reco_MET > 120 and MHT > 120 and ht_z_add > 900:
                        h_genmet_mhtmet120_pfht900.Fill(m.pt())
                if reco_MET > 120 and MHT > 120 and ht_z_add > 1050:
                        h_genmet_mhtmet120_pfht1050.Fill(m.pt())
		if reco_MET > 120 and MHT > 120:
			h_genmet_mhtmet120.Fill(m.pt())



outFile = ROOT.TFile.Open("Rinv_0p3_pfmetmht.root" ,"RECREATE")
outFile.cd()
h_MHT.Write()
h_genmet.Write()
h_genmet_mhtmet120.Write()
h_genmet_mhtmet120_pfjet450.Write()
h_genmet_mhtmet120_pfjet500.Write()
h_genmet_mhtmet120_pfjet550.Write()
h_genmet_mhtmet120_pfht800.Write()
h_genmet_mhtmet120_pfht900.Write()
h_genmet_mhtmet120_pfht1050.Write()
outFile.Close()
print "# of events", count
end = datetime.now()
print("end time:      "),end
