from CRABClient.UserUtilities import config
config = config()

#config.section_('General')
config.General.requestName = 'TTToHadronic_TuneCP5_13TeV_powheg-pythia8_DIGI-RECO'
config.General.workArea = 'crab_mc'
config.General.transferOutputs = True
config.General.transferLogs = True

#config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'digiToRecoStep_withPU_cfg.py'
config.JobType.maxMemoryMB = 4000

config.Data.inputDBS = 'phys03'
config.JobType.allowUndistributedCMSSW = True
config.Data.userInputFiles = open('TTToHadronic_TuneCP5_13TeV_powheg-pythia8_GEN-SIM.txt').readlines()
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1 
config.Data.outputPrimaryDataset = 'TTToHadronic_TuneCP5_13TeV_powheg-pythia8'

config.Data.outLFNDirBase = '/store/group/lpcml/bbbam/MCGeneration'
config.Data.publication = True 
config.Site.storageSite = 'T3_US_FNALLPC'
config.Data.outputDatasetTag = config.General.requestName
