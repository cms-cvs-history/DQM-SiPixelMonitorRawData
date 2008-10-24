import FWCore.ParameterSet.Config as cms

SiPixelRawDataErrorSource = cms.EDFilter("SiPixelRawDataErrorSource",
    src = cms.InputTag("siPixelDigis"),
    outputFile = cms.string('Pixel_DQM_Error.root'),
    saveFile = cms.untracked.bool(False),
    isPIB = cms.untracked.bool(False),
    slowDown = cms.untracked.bool(False),
    reducedSet = cms.untracked.bool(False),
    modOn = cms.untracked.bool(True),
    ladOn = cms.untracked.bool(False),
    layOn = cms.untracked.bool(False),
    phiOn = cms.untracked.bool(False),
    ringOn = cms.untracked.bool(False),
    bladeOn = cms.untracked.bool(False),
    diskOn = cms.untracked.bool(False)    
)


