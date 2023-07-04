from CRABClient.UserUtilities import config
config = config()

#config.section_('General')
config.General.requestName = 'DYToEE_M-50_13TeV-powheg_pythia8_DIGI-RECO'
config.General.workArea = 'crab_mc'
config.General.transferOutputs = True
config.General.transferLogs = True

#config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'digiToRecoStep_withPU_cfg.py'
config.JobType.maxMemoryMB = 4000

config.Data.inputDBS = 'phys03'
config.JobType.allowUndistributedCMSSW = True
#config.Data.inputDataset ='/DYToEE_M-50_13TeV-powheg_pythia8/lpcml-crab_DYToEE_M-50_13TeV-powheg_pythia8_GEN-SIM-LHEoutput-7e042a9e77bd8c54647ef57d77831daa/USER'
config.Data.userInputFiles = open('DYToEE_M-50_13TeV-powheg_pythia8_GEN-SIM.txt').readlines()
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1 
config.Data.outputPrimaryDataset = 'DYToEE_M-50_13TeV-powheg_pythia8'

config.Data.outLFNDirBase = '/store/group/lpcml/rchudasa/MCGeneration'
config.Data.publication = True 
config.Site.storageSite = 'T3_US_FNALLPC'
config.Data.outputDatasetTag = config.General.requestName
