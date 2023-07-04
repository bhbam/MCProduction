from CRABClient.UserUtilities import config
config = config()
# See parameter defintions here: https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile#CRAB_configuration_parameters

# Local job directory will be created in:
config.General.requestName = 'Upsilon1s_ToTauTau_Hadronic_tauDR0p4_pythia8_validationML_GEN_SIM_dataset_1'
config.General.workArea = 'crab_MC'
config.General.transferOutputs = True
config.General.transferLogs = True

# CMS cfg file goes here:
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'Upsilon1SToTauTau_Hadronic_tauDR0p4_eta0To2p4_pythia8_validationML_GEN_SIM_cfg.py'
config.Data.outputPrimaryDataset = 'Upsilon1s_ToTauTau_Hadronic_tauDR0p4_eta0To2p4_pythia8_validationML_dataset_1'

#config.JobType.maxMemoryMB = 2800

# Define units per job here:
config.JobType.allowUndistributedCMSSW = True
config.JobType.eventsPerLumi=6000
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 30000 # units: large number is given because Upsilon1SToTauTau has filters and cut on pt and eta
# config.Data.unitsPerJob = 300 # units: large number is given because Upsilon1SToTauTau has filters and cut on pt and eta
NJOBS = 1000
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = True

# Output files will be stored in config.Site.storageSite at directory:
config.Data.outLFNDirBase = '/store/group/lpcml/bbbam/MCGeneration'
config.Site.storageSite = 'T3_US_FNALLPC'
