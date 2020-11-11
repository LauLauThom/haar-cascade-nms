# Changelog
All notable changes to this project will be documented in this file.  

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [1.1.0] - 2020-11-
### Changed
- Dont do NMS when nObject=1: just return the best detection if score>threshold
- detectAndFilter function signature has now first the minSize, maxSize and then scaleFactor (this is a breaking change !!)
- Docstring for parameters of detectAndFilter
- Default values for most parameters of detectAndFilter except minSize/maxSize

### Added
- test.py

## [1.0.0] - 2020-09-16
- initial stable release
