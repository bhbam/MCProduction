from CRABClient.UserUtilities import config#, getUsernameFromSiteDB
config = config()
# See parameter defintions here: https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile#CRAB_configuration_parameters


# To submit to crab:
# crab submit -c crabConfig_data.py
# To check job status:
# crab status -d <config.General.workArea>/<config.General.requestName>
# To resubmit jobs:
# crab resubmit -d <config.General.workArea>/<config.General.requestName>
Mass = '8' #3p7,4,5,6,8,10,12,14
# Local job directory will be created in:

config.General.workArea        = 'crab_MC'
config.General.requestName     = 'Unboosted_sim_HToAATo4Tau_Hadronic_tauDR0p4_M%s_ctau0To3_eta0To2p4_pythia8_2018UL'%Mass
config.General.transferOutputs = True
config.General.transferLogs    = True

# CMS cfg file goes here:
config.JobType.pluginName  = 'Analysis' # mass > 8 use this
config.JobType.psetName    = 'sim_HToAATo4Tau_RunIISummer20UL18_00066_1_withPU_cfg.py' # cms cfg file for generating events
config.JobType.maxMemoryMB = 5000 #5000
# config.JobType.numCores = 4

config.Data.inputDBS = 'phys03'
config.JobType.allowUndistributedCMSSW = True
# Define input and units per job here:
if Mass=="8":
    config.Data.inputDataset = '/Unboosted_gen_HToAATo4Tau_Hadronic_tauDR0p4_M8_ctau0To3_eta0To2p4_pythia8_2018UL_lessPerFile/bhbam-crab_Unboosted_gen_HToAATo4Tau_Hadronic_tauDR0p4_M8_ctau0To3_eta0To2p4_pythia8_2018UL_lessPerFile-32756e1c2f1fb6205fbab69b71f9d84d/USER'
# config.Data.userInputFiles = open('MLAnalyzer/list_gen_sim_aToTauTau_m3p6To15.txt').readlines()

config.Data.splitting      = 'FileBased'
config.Data.unitsPerJob    = 1  # units: as defined by config.Data.splitting
config.Data.totalUnits     = -1 # -1: all inputs. total jobs submitted = totalUnits / unitsPerJob. cap of 10k jobs per submission
config.Data.publication    = True

config.Data.outLFNDirBase = '/store/user/bhbam/MCGeneration'
config.Site.storageSite = 'T3_US_FNALLPC'
config.Data.outputDatasetTag = config.General.requestName
