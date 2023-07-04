from CRABClient.UserUtilities import config
config = config()

#config.section_('General')
config.General.requestName = 'DYToEE_M-50_13TeV-powheg_pythia8_GEN-SIM'
config.General.workArea = 'crab_mc'
config.General.transferOutputs = True
config.General.transferLogs = True

#config.section_('JobType')
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'DYToEE_M-50_13TeV-powheg_pythia8_GEN-SIM_cfg.py'
config.Data.outputPrimaryDataset = 'DYToEE_M-50_13TeV-powheg_pythia8'

config.JobType.allowUndistributedCMSSW = True
#config.JobType.numCores = 8
#config.JobType.eventsPerLumi=100
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob =1000
NJOBS = 1000
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS

config.Data.outLFNDirBase = '/store/group/lpcml/rchudasa/MCGeneration'
#config.Data.publication = False 
#config.Data.publication = True 
config.Site.storageSite = 'T3_US_FNALLPC'