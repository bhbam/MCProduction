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
config.General.requestName     = 'aToTauTau_Hadronic_tauDR0p4_m14To17p2_pythia8_DIGI_RECO_dataset_2'
config.General.transferOutputs = True
config.General.transferLogs    = True

# CMS cfg file goes here:
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName    = 'digiToRecoStep_withPU_cfg.py' # cms cfg file for generating events
config.JobType.maxMemoryMB = 5000
config.Data.inputDBS = 'phys03'
config.JobType.allowUndistributedCMSSW = True
# Define input and units per job here:
# config.Data.inputDataset = '/aToTauTau_Hadronic_tauDR0p4_m3p6To16_pT30To180_ctau0To3_eta0To1p4_pythia8_unbiased4ML/lpcml-crab_aToTauTau_Hadronic_tauDR0p4_m3p6To16_pythia8_GEN-SIM-30fd60d68136aed98eaedb7648aca9e6/USER'
# config.Data.inputDataset = '/aToTauTau_Hadronic_tauDR0p4_m3p6To16_pT30To180_ctau0To3_eta0To1p4_pythia8_unbiased4ML_dataset_1/lpcml-crab_aToTauTau_Hadronic_tauDR0p4_m3p6To16_pythia8_GEN_SIM_dataset_1-acb670bf06898785de589cab54f2bbbb/USER'
# config.Data.inputDataset = '/aToTauTau_Hadronic_tauDR0p4_m14To17p2_pT30To180_ctau0To3_eta0To2p4_pythia8/lpcml-crab_aToTauTau_Hadronic_tauDR0p4_m14To17p2_pythia8_GEN_SIM-b7ea9f388d4912cd53244dd52524e913/USER'
config.Data.inputDataset = '/aToTauTau_Hadronic_tauDR0p4_m14To17p2_pT30To180_ctau0To3_eta0To2p4_pythia8_dataset_2/lpcml-crab_aToTauTau_Hadronic_tauDR0p4_m14To17p2_pythia8_GEN_SIM_dataset_2-b7ea9f388d4912cd53244dd52524e913/USER'
# config.Data.userInputFiles = open('MLAnalyzer/list_gen_sim_aToTauTau_m3p6To15.txt').readlines()
config.Data.splitting      = 'FileBased'
config.Data.unitsPerJob    = 1  # units: as defined by config.Data.splitting
config.Data.totalUnits     = -1 # -1: all inputs. total jobs submitted = totalUnits / unitsPerJob. cap of 10k jobs per submission
config.Data.publication    = True

# Output files will be stored in config.Site.storageSite at directory:
# <config.Data.outLFNDirBase>/<config.Data.outputPrimaryDataset>/<config.Data.outputDatasetTag>/
config.Data.outLFNDirBase = '/store/group/lpcml/bbbam/MCGeneration'

config.Site.storageSite = 'T3_US_FNALLPC'
config.Data.outputDatasetTag = config.General.requestName
