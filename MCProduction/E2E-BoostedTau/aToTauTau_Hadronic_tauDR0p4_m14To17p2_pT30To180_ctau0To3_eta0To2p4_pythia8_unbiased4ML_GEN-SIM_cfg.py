# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: SingleNuE10_cfi.py --python_filename aToTauTau_GEN-SIM_cfg.py --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --fileout file:aToTauTau_GEN-SIM.root --conditions 106X_upgrade2018_realistic_v4 --beamspot Realistic25ns13TeVEarly2018Collision --step GEN,SIM --geometry DB:Extended --era Run2_2018 --no_exec --mc -n 1000
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2018_cff import Run2_2018

process = cms.Process('SIM',Run2_2018)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13TeVEarly2018Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.MessageLogger = cms.Service("MessageLogger",
        destinations   = cms.untracked.vstring('detailedInfo'),
        categories      = cms.untracked.vstring('eventNumber'),
        detailedInfo    = cms.untracked.PSet(eventNumber = cms.untracked.PSet(reportEvery = cms.untracked.int32(1000))),
)

process.genHToTauTauFilter = cms.EDFilter("GenHToTauTauFilter",
    src       = cms.InputTag("genParticles"), #GenParticles collection as input
    nHiggs    = cms.double(1),                #Number of pdgID=25 candidates
    tauPtCut  = cms.double(1.0),              #at least a GenTau with this minimum pT
    tauEtaCut = cms.double(2.4),              #GenTau eta
    taudRCut  = cms.double(0.4)               #GenTauTau cut
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(500000)
    # input = cms.untracked.int32(3000000)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True)

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('SingleNuE10_cfi.py nevts:1000'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(1),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    fileName = cms.untracked.string('file:aToTauTau_GEN-SIM.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.XMLFromDBSource.label = cms.string("Extended")
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_upgrade2018_realistic_v4', '')

process.generator = cms.EDFilter("Pythia8PtGunV3",
    PGunParameters = cms.PSet(
        AddAntiParticle = cms.bool(True),
        MaxCTau = cms.double(3.0),
        MaxEta = cms.double(2.4),
        MaxMass = cms.double(17.2),
        MaxPhi = cms.double(3.14159265359),
        MaxPt = cms.double(180.0),
        MinCTau = cms.double(0.0),
        MinEta = cms.double(-2.4),
        MinMass = cms.double(14),
        MinPhi = cms.double(-3.14159265359),
        MinPt = cms.double(30.0),
        ParticleID = cms.vint32(25)
    ),
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring('processParameters'),
        processParameters = cms.vstring(
            '25:onMode = off',
            '25:onIfMatch = 15 -15',
            '15:onMode = on',
            '15:offIfAny = 11 -11 13 -13'
        )
    ),
    Verbosity = cms.untracked.int32(0),
    firstRun = cms.untracked.uint32(1),
    maxEventsToPrint = cms.untracked.int32(1),
    psethack = cms.string('a to tautau pTgun'),
    pythiaHepMCVerbosity = cms.untracked.bool(True),
    pythiaPylistVerbosity = cms.untracked.int32(1)
)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen+process.genHToTauTauFilter)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path).insert(0, process.generator)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
