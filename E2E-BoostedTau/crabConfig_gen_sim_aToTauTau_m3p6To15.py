from CRABClient.UserUtilities import config
config = config()
# See parameter defintions here: https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile#CRAB_configuration_parameters

# Local job directory will be created in:
config.General.requestName = 'aToTauTau_Hadronic_tauDR0p4_m3p6To16_pythia8_GEN_SIM_dataset_2'
config.General.workArea = 'crab_MC'
config.General.transferOutputs = True
config.General.transferLogs = True

# CMS cfg file goes here:
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'aToTauTau_Hadronic_tauDR0p4_m3p6To15_pT30To180_ctau0To3_eta0To2p4_pythia8_unbiased4ML_GEN-SIM_cfg.py'
config.Data.outputPrimaryDataset = 'aToTauTau_Hadronic_tauDR0p4_m3p6To16_pT30To180_ctau0To3_eta0To1p4_pythia8_unbiased4ML_dataset_2'

#config.JobType.maxMemoryMB = 2800

# Define units per job here:
config.JobType.allowUndistributedCMSSW = True
config.JobType.eventsPerLumi=60000
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 3000000 # units: large number is given because aToTauTau has filters and cut on pt and eta
NJOBS = 10000
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = True

# Output files will be stored in config.Site.storageSite at directory:
config.Data.outLFNDirBase = '/store/group/lpcml/bbbam/MCGeneration'
config.Site.storageSite = 'T3_US_FNALLPC'
