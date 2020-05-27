#include<string>
#include<iostream>
#include<fstream>
#include<sstream>
#include<iomanip>
#include<map>
  
#include "TH1.h"
#include "TH1F.h"
#include "vector"
#include "TEfficiency.h"
#include <TGraph2D.h>
#include "TString.h"
#include "TSystem.h"
#include "TStyle.h"
#include "TPad.h"

int dolog=0;
//void eff(const char* outputFile)
void pfhtjet_0p3()
{ 
  gStyle->SetOptStat(111111);
 
	TCanvas* canv = new TCanvas("canv","canv");
	canv->SetLogy();

        TCanvas* canv1 = new TCanvas("canv1","canv1");
        canv1->SetLogy();

        TCanvas* canv2 = new TCanvas("canv2","canv2");
        canv2->SetLogy();

        TCanvas* canv3 = new TCanvas("canv3","canv3");
        canv3->SetLogy();

	TFile *bfile = new TFile("Rinv_0p3_pfhtjetak8.root");//rinv_0p8
       	
        TH1F* h_total = (TH1F*)bfile->Get("h_genht");
        TH1F* h_pfjet450 = (TH1F*)bfile->Get("h_genht_pfjet450");
        TH1F* h_pfjet500 = (TH1F*)bfile->Get("h_genht_pfjet500");
        TH1F* h_pfjet550 = (TH1F*)bfile->Get("h_genht_pfjet550");
        TH1F* h_ak8pfjet450 = (TH1F*)bfile->Get("h_genht_ak8pfjet450");
        TH1F* h_ak8pfjet500 = (TH1F*)bfile->Get("h_genht_ak8pfjet500");
        TH1F* h_ak8pfjet550 = (TH1F*)bfile->Get("h_genht_ak8pfjet550");
        TH1F* h_pfht800 = (TH1F*)bfile->Get("h_genht_pfht800");
        TH1F* h_pfht900 = (TH1F*)bfile->Get("h_genht_pfht900");
        TH1F* h_pfht1050 = (TH1F*)bfile->Get("h_genht_pfht1050");
        TH1F* h_pfgenht = (TH1F*)bfile->Get("h_genht");
	
        TEfficiency* pfjet450 = 0;
        TEfficiency* pfjet500 = 0;
        TEfficiency* pfjet550 = 0;
        TEfficiency* ak8pfjet450 = 0;
        TEfficiency* ak8pfjet500 = 0;
        TEfficiency* ak8pfjet550 = 0;
        TEfficiency* pfht800 = 0;
        TEfficiency* pfht900 = 0;
        TEfficiency* pfht1050 = 0;

        pfjet450 = new TEfficiency(*h_pfjet450,*h_total);
        pfjet450->SetStatisticOption(TEfficiency::kFCP);//kFCP, kBBayesian, kFNormal, kMidP
        pfjet450->SetConfidenceLevel(0.68);

        pfjet500 = new TEfficiency(*h_pfjet500,*h_total);
        pfjet500->SetStatisticOption(TEfficiency::kFCP);//kFCP, kBBayesian, kFNormal, kMidP
        pfjet500->SetConfidenceLevel(0.68);

        pfjet550 = new TEfficiency(*h_pfjet550,*h_total);
        pfjet550->SetStatisticOption(TEfficiency::kFCP);//kFCP, kBBayesian, kFNormal, kMidP
        pfjet550->SetConfidenceLevel(0.68);

        ak8pfjet450 = new TEfficiency(*h_ak8pfjet450,*h_total);
        ak8pfjet450->SetStatisticOption(TEfficiency::kFCP);//kFCP, kBBayesian, kFNormal, kMidP
        ak8pfjet450->SetConfidenceLevel(0.68);

        ak8pfjet500 = new TEfficiency(*h_ak8pfjet500,*h_total);
        ak8pfjet500->SetStatisticOption(TEfficiency::kFCP);//kFCP, kBBayesian, kFNormal, kMidP
        ak8pfjet500->SetConfidenceLevel(0.68);

        ak8pfjet550 = new TEfficiency(*h_ak8pfjet550,*h_total);
        ak8pfjet550->SetStatisticOption(TEfficiency::kFCP);//kFCP, kBBayesian, kFNormal, kMidP
        ak8pfjet550->SetConfidenceLevel(0.68);

        pfht800 = new TEfficiency(*h_pfht800,*h_total);
        pfht800->SetStatisticOption(TEfficiency::kFCP);//kFCP, kBBayesian, kFNormal, kMidP
        pfht800->SetConfidenceLevel(0.68);

        pfht900 = new TEfficiency(*h_pfht900,*h_total);
        pfht900->SetStatisticOption(TEfficiency::kFCP);//kFCP, kBBayesian, kFNormal, kMidP
        pfht900->SetConfidenceLevel(0.68);

        pfht1050 = new TEfficiency(*h_pfht1050,*h_total);
        pfht1050->SetStatisticOption(TEfficiency::kFCP);//kFCP, kBBayesian, kFNormal, kMidP
        pfht1050->SetConfidenceLevel(0.68);

        canv->cd();
        pfjet550->SetLineColor(3);
        pfjet500->SetLineColor(4);
	pfjet450->SetLineColor(2);
        pfjet550->Draw("A");
        pfjet500->Draw("SAME");
        pfjet450->Draw("SAME");
        pfjet550->SetTitle("PFJet     Efficiency Vs genHT; genHT; efficiency (#epsilon)");
        TLegend *legend = new TLegend(0.6,0.7,0.7,0.5);
        legend->Draw();
        legend->AddEntry(pfjet550,"pfjet550","L");
        legend->AddEntry(pfjet500,"pfjet500","L");
        legend->AddEntry(pfjet450,"pjfet450","L");
        legend->Draw("SAME");
        canv->Modified();
        canv->Update();
        //canv->SaveAs("Plot_pfjetxxx_rinv0px.png");

        canv1->cd();
        ak8pfjet550->SetLineColor(3);
        ak8pfjet500->SetLineColor(4);
        ak8pfjet450->SetLineColor(2);
        ak8pfjet550->Draw("A");
        ak8pfjet500->Draw("SAME");
        ak8pfjet450->Draw("SAME");
        ak8pfjet550->SetTitle("AK8PFJet     Efficiency Vs genHT; genHT; efficiency (#epsilon)");
        TLegend *legend1 = new TLegend(0.6,0.7,0.7,0.5);
        legend1->Draw();
        legend1->AddEntry(ak8pfjet550,"ak8pfjet550","L");
        legend1->AddEntry(ak8pfjet500,"ak8pfjet500","L");
        legend1->AddEntry(ak8pfjet450,"ak8pjfet450","L");
        legend1->Draw("SAME");
        canv1->Modified();
        canv1->Update();
        //canv1->SaveAs("Plot_ak8pfjetxxx_rinv0px.png");

        canv2->cd();
        pfht1050->SetLineColor(3);
        pfht900->SetLineColor(4);
        pfht800->SetLineColor(2);
        pfht1050->Draw("A");
        pfht900->Draw("SAME");
        pfht800->Draw("SAME");
        pfht1050->SetTitle("PFHT     Efficiency Vs genHT; genHT; efficiency (#epsilon)");
        TLegend *legend2 = new TLegend(0.6,0.7,0.7,0.5);
        legend2->Draw();
        legend2->AddEntry(pfht1050,"pfht1050","L");
        legend2->AddEntry(pfht900,"pfht900","L");
        legend2->AddEntry(pfht800,"pfht800","L");
        legend2->Draw("SAME");
        canv2->Modified();
        canv2->Update();
	//canv2->SaveAs("Plot_pfhtxxx_rinv0px.png");
	

        canv3->cd();
        pfht1050->SetLineColor(4);
        pfjet550->SetLineColor(3);
        pfjet500->SetLineColor(2);
        pfht1050->Draw("A");
        pfjet550->Draw("SAME");
        pfjet500->Draw("SAME");
        pfht1050->SetTitle("2017     Efficiency Vs genHT; genHT; efficiency (#epsilon)");
        TLegend *legend3 = new TLegend(0.6,0.7,0.7,0.5);
        legend3->Draw();
        legend3->AddEntry(pfjet500,"pfjet500","L");
        legend3->AddEntry(pfjet550,"pfjet550","L");
        legend3->AddEntry(pfht1050,"pfht1050","L");
        legend3->Draw("SAME");
        canv3->Modified();
        canv3->Update();
        //canv3->SaveAs("Plot_2017_rinv0px.png");


	TFile *f = new TFile("eff_pfhtjet.root","RECREATE");
	pfht800->Write();
        pfht900->Write();
        pfht1050->Write();
        pfjet450->Write();
        pfjet500->Write();
        pfjet550->Write();
        ak8pfjet450->Write();
        ak8pfjet500->Write();
        ak8pfjet550->Write();
	f->Close();
}
