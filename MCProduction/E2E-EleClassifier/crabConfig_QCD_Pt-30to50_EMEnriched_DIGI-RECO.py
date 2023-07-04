from CRABClient.UserUtilities import config
config = config()

#config.section_('General')
config.General.requestName = 'QCD_Pt-30to50_EMEnriched_DIGI-RECO'
config.General.workArea = 'crab_mc'
config.General.transferOutputs = True
config.General.transferLogs = True

#config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'digiToRecoStep_withPU_cfg.py'
config.JobType.maxMemoryMB = 4000

config.Data.inputDBS = 'phys03'
config.JobType.allowUndistributedCMSSW = True
config.Data.inputDataset ='/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV_pythia8/lpcml-crab_QCD_Pt-30to50_EMEnriched_GEN-SIM-2bb5fe7797b965a1ce4529f6aa7829b1/USER'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1 

config.Data.outLFNDirBase = '/store/group/lpcml/rchudasa/MCGeneration'
config.Data.publication = True 
config.Site.storageSite = 'T3_US_FNALLPC'
config.Data.outputDatasetTag = config.General.requestName
