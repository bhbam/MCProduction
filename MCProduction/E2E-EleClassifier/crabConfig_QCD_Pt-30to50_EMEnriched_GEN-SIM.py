from CRABClient.UserUtilities import config
config = config()

#config.section_('General')
config.General.requestName = 'QCD_Pt-30to50_EMEnriched_GEN-SIM'
config.General.workArea = 'crab_mc'
config.General.transferOutputs = True
config.General.transferLogs = True

#config.section_('JobType')
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV_pythia8_GEN-SIM_cfg.py'
config.Data.outputPrimaryDataset = 'QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV_pythia8'

config.JobType.allowUndistributedCMSSW = True
#config.JobType.numCores = 8
config.JobType.eventsPerLumi=6000
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 20000
NJOBS = 1000
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS

config.Data.outLFNDirBase = '/store/group/lpcml/rchudasa/MCGeneration'
#config.Data.publication = False 
config.Data.publication = True 
config.Site.storageSite = 'T3_US_FNALLPC'
