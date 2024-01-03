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
Mass = '8' #3p7,4,5,6,8,10,12,14
# Local job directory will be created in:
# <config.General.workArea>/<config.General.requestName>
config.General.workArea        = 'crab_MC'
config.General.requestName     = 'sim_HToAATo4Tau_Hadronic_tauDR0p4_M%s_ctau0To3_eta0To2p4_pythia8_2018UL'%Mass
config.General.transferOutputs = True
config.General.transferLogs    = True

# CMS cfg file goes here:
config.JobType.pluginName  = 'Analysis' # mass > 8 use this
# config.JobType.pluginName  = 'PrivateMC' # mass <10 use this

config.JobType.psetName    = 'sim_HToAATo4Tau_RunIISummer20UL18_00066_1_withPU_cfg.py' # cms cfg file for generating events
config.JobType.maxMemoryMB = 5000 #5000
# config.JobType.numCores = 4

config.Data.inputDBS = 'phys03'
config.JobType.allowUndistributedCMSSW = True
# Define input and units per job here:
if Mass=="3p7":
    config.Data.inputDataset = '/gen_HToAATo4Tau_Hadronic_tauDR0p4_M3p7_ctau0To3_eta0To2p4_pythia8_2018UL_lessPerFile/lpcml-crab_gen_HToAATo4Tau_Hadronic_tauDR0p4_M3p7_ctau0To3_eta0To2p4_pythia8_2018UL_lessPerFile-8426bd16601bf2a66b062db1a55d9485/USER'
if Mass=="4":
    config.Data.inputDataset = '/gen_HToAATo4Tau_Hadronic_tauDR0p4_M4_ctau0To3_eta0To2p4_pythia8_2018UL_lessPerFile/lpcml-crab_gen_HToAATo4Tau_Hadronic_tauDR0p4_M4_ctau0To3_eta0To2p4_pythia8_2018UL_lessPerFile-dad6354eeaf1e4e40fa03bd2d790f1fe/USER'
if Mass=="5":
    config.Data.inputDataset = '/gen_HToAATo4Tau_Hadronic_tauDR0p4_M5_ctau0To3_eta0To2p4_pythia8_2018UL_lessPerFile/lpcml-crab_gen_HToAATo4Tau_Hadronic_tauDR0p4_M5_ctau0To3_eta0To2p4_pythia8_2018UL_lessPerFile-ee16056bdc35642e4c22a7e10301bfe2/USER'
if Mass=="6":
    config.Data.inputDataset = '/gen_HToAATo4Tau_Hadronic_tauDR0p4_M6_ctau0To3_eta0To2p4_pythia8_2018UL_lessPerFile/lpcml-crab_gen_HToAATo4Tau_Hadronic_tauDR0p4_M6_ctau0To3_eta0To2p4_pythia8_2018UL_lessPerFile-8ea7f45ed94535803355813970e18ce4/USER'
if Mass=="8":
    config.Data.inputDataset = '/gen_HToAATo4Tau_Hadronic_tauDR0p4_M8_ctau0To3_eta0To2p4_pythia8_2018UL_lessPerFile/lpcml-crab_gen_HToAATo4Tau_Hadronic_tauDR0p4_M8_ctau0To3_eta0To2p4_pythia8_2018UL_lessPerFile-32756e1c2f1fb6205fbab69b71f9d84d/USER'
if Mass=="10":
    config.Data.inputDataset = '/gen_HToAATo4Tau_Hadronic_tauDR0p4_M10_ctau0To3_eta0To2p4_pythia8_2018UL/lpcml-crab_gen_HToAATo4Tau_Hadronic_tauDR0p4_M10_ctau0To3_eta0To2p4_pythia8_2018UL-720d454354039bb04c7bc8eed758df57/USER'
if Mass=="12":
    config.Data.inputDataset = '/gen_HToAATo4Tau_Hadronic_tauDR0p4_M12_ctau0To3_eta0To2p4_pythia8_2018UL/lpcml-crab_gen_HToAATo4Tau_Hadronic_tauDR0p4_M12_ctau0To3_eta0To2p4_pythia8_2018UL-25e993739bee5acaaa9abf6f5020d93b/USER'
if Mass=="14":
    config.Data.inputDataset = '/gen_HToAATo4Tau_Hadronic_tauDR0p4_M14_ctau0To3_eta0To2p4_pythia8_2018UL/lpcml-crab_gen_HToAATo4Tau_Hadronic_tauDR0p4_M14_ctau0To3_eta0To2p4_pythia8_2018UL-67152ee38932d0d14dc2312e06f15c07/USER'
# config.Data.userInputFiles = open('MLAnalyzer/list_gen_sim_aToTauTau_m3p6To15.txt').readlines()

# for m >8 use this to process all events.
config.Data.splitting      = 'FileBased'
config.Data.unitsPerJob    = 1  # units: as defined by config.Data.splitting
config.Data.totalUnits     = -1 # -1: all inputs. total jobs submitted = totalUnits / unitsPerJob. cap of 10k jobs per submission

config.Data.publication    = True


# # for m < 10 use this but you have final number of events.
# config.Data.splitting = 'EventAwareLumiBased'
# config.Data.unitsPerJob = 1
# NJOBS = 2
# config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
# config.Data.totalUnits = -1
# config.Data.outputPrimaryDataset = 'sim_HToAATo4Tau_Hadronic_tauDR0p4_M%s_ctau0To3_eta0To2p4_pythia8_2018UL'%Mass

# Output files will be stored in config.Site.storageSite at directory:
# <config.Data.outLFNDirBase>/<config.Data.outputPrimaryDataset>/<config.Data.outputDatasetTag>/
config.Data.outLFNDirBase = '/store/group/lpcml/bbbam/MCGeneration'
# config.Data.outLFNDirBase = '/store/user/bhbam/MCGeneration'

config.Site.storageSite = 'T3_US_FNALLPC'
config.Data.outputDatasetTag = config.General.requestName
