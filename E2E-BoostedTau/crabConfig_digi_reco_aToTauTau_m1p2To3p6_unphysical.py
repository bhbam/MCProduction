from CRABClient.UserUtilities import config#, getUsernameFromSiteDB
config = config()
# See parameter defintions here: https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile#CRAB_configuration_parameters

# CFG = 'sim_HToAATo4Tau_RunIISummer20UL18_00066_1_cfg'

# To submit to crab:
# crab submit -c crabConfig_data.py
# To check job status:
# crab status -d <config.General.workArea>/<config.General.requestName>
# To resubmit jobs:
# crab resubmit -d <config.General.workArea>/<config.General.requestName>

# Local job directory will be created in:
# <config.General.workArea>/<config.General.requestName>
config.General.workArea        = 'crab_MC'
config.General.requestName     = 'sim_aToTauTau_Hadronic_tauDR0p4_m1p2To3p6_pythia8_DIGI_RECO_unphysical'
config.General.transferOutputs = True
config.General.transferLogs    = True

# CMS cfg file goes here:
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName    = 'digiToRecoStep_withPU_cfg.py' # cms cfg file for generating events
config.JobType.maxMemoryMB = 5000
# config.Data.inputDBS = 'phys03'
# config.JobType.allowUndistributedCMSSW = True
# Define input and units per job here:
# config.Data.inputDataset = '/aToTauTau_Hadronic_tauDR0p4_m3p6To16_pT30To180_ctau0To3_eta0To1p4_pythia8_unbiased4ML/lpcml-crab_aToTauTau_Hadronic_tauDR0p4_m3p6To16_pythia8_GEN-SIM-30fd60d68136aed98eaedb7648aca9e6/USER'
# config.Data.inputDataset = '/aToTauTau_Hadronic_tauDR0p4_m3p6To16_pT30To180_ctau0To3_eta0To1p4_pythia8_unbiased4ML_dataset_1/lpcml-crab_aToTauTau_Hadronic_tauDR0p4_m3p6To16_pythia8_GEN_SIM_dataset_1-acb670bf06898785de589cab54f2bbbb/USER'
# config.Data.inputDataset = '/aToTauTau_Hadronic_tauDR0p4_m3p6To16_pT30To180_ctau0To3_eta0To1p4_pythia8_unbiased4ML_dataset_2/lpcml-crab_aToTauTau_Hadronic_tauDR0p4_m3p6To16_pythia8_GEN_SIM_dataset_2-29e4fa1151f2cddaf0b8e8ef6a2a93fe/USER'
# config.Data.userInputFiles = open('list_unphysical_sample_test.txt').readlines()
# l = open('list_one.txt').readlines()
# l2 = [x.split('\n')[0] for x in l]
# config.Data.userInputFiles = l2
# config.Data.userInputFiles = open('list_aToTauTau_Hadronic_tauDR0p4_m3p6To16_pythia8_DIGI_RECO.txt').readlines()
config.Data.userInputFiles = open('list_gen_unphysical_files.txt').readlines()
# config.Data.userInputFiles = ['root://cmsxrootd.fnal.gov//store/group/lpcml/bbbam/MCGeneration/unphysical_sample_test/aToTauTau_Hadronic_tauDR0p4_m1p2To3p6_pT30To180_ctau0To3_eta0To2p4_unphysical/crab_aToTauTau_Hadronic_tauDR0p4_m1p2To3p6_pythia8_GEN_unphysical/230929_033832/0000/aToTauTau_GEN_SIM_unphysical_1.root',
# 'root://cmsxrootd.fnal.gov//store/group/lpcml/bbbam/MCGeneration/unphysical_sample_test/aToTauTau_Hadronic_tauDR0p4_m1p2To3p6_pT30To180_ctau0To3_eta0To2p4_unphysical/crab_aToTauTau_Hadronic_tauDR0p4_m1p2To3p6_pythia8_GEN_unphysical/230929_033832/0000/aToTauTau_GEN_SIM_unphysical_10.root']
config.Data.splitting      = 'FileBased'
config.Data.unitsPerJob    = 1  # units: as defined by config.Data.splitting
config.Data.totalUnits     = -1 # -1: all inputs. total jobs submitted = totalUnits / unitsPerJob. cap of 10k jobs per submission
config.Data.publication    = True

# Output files will be stored in config.Site.storageSite at directory:
# <config.Data.outLFNDirBase>/<config.Data.outputPrimaryDataset>/<config.Data.outputDatasetTag>/

# config.Data.ignoreLocality = True
# config.Site.whitelist = ['T3_US_FNALLPC']
# config.Site.ignoreGlobalBlacklist = True
config.Site.storageSite = 'T3_US_FNALLPC'
config.Data.outLFNDirBase = '/store/group/lpcml/bbbam/MCGeneration'
config.Data.outputPrimaryDataset = 'aToTauTau_Hadronic_tauDR0p4_m1p2To3p6_pythia8_DIGI_RECO_unphysical'
config.Data.outputDatasetTag = config.General.requestName
