import FWCore.ParameterSet.Config as cms

process = cms.Process("SiPixelMonitorRawDataProcess")
process.load("Geometry.TrackerSimData.trackerSimGeometryXML_cfi")

process.load("Geometry.TrackerGeometryBuilder.trackerGeometry_cfi")

process.load("Geometry.TrackerNumberingBuilder.trackerNumberingGeometry_cfi")

process.load("DQM.SiPixelMonitorRawData.SiPixelMonitorRawData_cfi")

process.load("DQMServices.Core.DQM_cfg")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)
process.source = cms.Source("PoolSource",
    debugFlag = cms.untracked.bool(True),
    debugVebosity = cms.untracked.uint32(10),
    fileNames = cms.untracked.vstring('file:digis.root')
)

process.LockService = cms.Service("LockService",
    labels = cms.untracked.vstring('source')
)

process.MessageLogger = cms.Service("MessageLogger",
    destinations = cms.untracked.vstring('debugmessages.txt')
)

process.p1 = cms.Path(process.SiPixelRawDataErrorSource)
process.SiPixelRawDataErrorSource.saveFile = True
process.SiPixelRawDataErrorSource.isPIB = False
process.SiPixelDigiSource.slowDown = False
process.DQM.collectorHost = ''

