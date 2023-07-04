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
config.General.requestName     = 'sim_HToAATo4Tau_Hadronic_tauDR0p4_M10_ctau0To3_eta0To2p4_pythia8_2018UL'
config.General.transferOutputs = True
config.General.transferLogs    = True

# CMS cfg file goes here:
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName    = 'sim_HToAATo4Tau_RunIISummer20UL18_00066_1_withPU_cfg.py' # cms cfg file for generating events
config.JobType.maxMemoryMB = 5000
config.Data.inputDBS = 'phys03'
config.JobType.allowUndistributedCMSSW = True
# Define input and units per job here:
config.Data.inputDataset = '/gen_HToAATo4Tau_Hadronic_tauDR0p4_M10_ctau0To3_eta0To2p4_pythia8_2018UL/lpcml-crab_gen_HToAATo4Tau_Hadronic_tauDR0p4_M10_ctau0To3_eta0To2p4_pythia8_2018UL-720d454354039bb04c7bc8eed758df57/USER'
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
